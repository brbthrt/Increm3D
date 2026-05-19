import os
import cv2
import numpy as np
import config
import utils
import features
import triangulation
import colors
import visualization


def main():
    img_files = sorted([f for f in os.listdir(config.IMG_DIR) if f.lower().endswith(('.ppm', '.jpg', '.png'))])
    sift, flann = features.get_features_detector()

    all_points_3d = []
    views = []

    for i, img_file in enumerate(img_files):
        img_path = os.path.join(config.IMG_DIR, img_file)
        img = cv2.imread(img_path)
        if img is None: continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kp, des = sift.detectAndCompute(gray, None)

        current_view = {
            'kp': kp,
            'des': des,
            'kp_to_3d': np.full(len(kp), -1, dtype=int),
            'P_ext': None
        }

        if i == 0:
            current_view['P_ext'] = np.eye(3, 4, dtype=np.float32)
            views.append(current_view)
            continue

        prev_view = views[i - 1]
        good = features.match_features(flann, prev_view['des'], current_view['des'])

        if i == 1:
            src_pts = np.float32([prev_view['kp'][m.queryIdx].pt for m in good])
            dst_pts = np.float32([current_view['kp'][m.trainIdx].pt for m in good])

            E, mask_e = cv2.findEssentialMat(src_pts, dst_pts, config.INTRINSIC, method=cv2.RANSAC, threshold=1.0)
            _, R, t, mask_p = cv2.recoverPose(E, src_pts, dst_pts, config.INTRINSIC, mask=mask_e)

            current_view['P_ext'] = np.hstack((R, t))
            idx_inliers = np.where(mask_p.ravel() == 1)[0]

            pts1_n = config.K_INV @ utils.cart2hom(src_pts[idx_inliers])
            pts2_n = config.K_INV @ utils.cart2hom(dst_pts[idx_inliers])
            pts3d = triangulation.linear_triangulation(pts1_n, pts2_n, prev_view['P_ext'], current_view['P_ext'])

            for idx_in, original_idx in enumerate(idx_inliers):
                all_points_3d.append(pts3d[:3, idx_in])
                g_idx = len(all_points_3d) - 1
                m = good[original_idx]
                prev_view['kp_to_3d'][m.queryIdx] = g_idx
                current_view['kp_to_3d'][m.trainIdx] = g_idx
        else:
            pts_3d_pnp, pts_2d_pnp, pnp_matches = [], [], []
            for m in good:
                if prev_view['kp_to_3d'][m.queryIdx] != -1:
                    pts_3d_pnp.append(all_points_3d[prev_view['kp_to_3d'][m.queryIdx]])
                    pts_2d_pnp.append(current_view['kp'][m.trainIdx].pt)
                    pnp_matches.append(m)

            if len(pts_3d_pnp) >= 10:
                success, rvec, tvec, inliers = cv2.solvePnPRansac(
                    np.array(pts_3d_pnp, dtype=np.float32), np.array(pts_2d_pnp, dtype=np.float32),
                    config.INTRINSIC, None)
                if success:
                    R, _ = cv2.Rodrigues(rvec)
                    current_view['P_ext'] = np.hstack((R, tvec))
                    if inliers is not None:
                        for idx in inliers.ravel():
                            m = pnp_matches[idx]
                            current_view['kp_to_3d'][m.trainIdx] = prev_view['kp_to_3d'][m.queryIdx]

            # Тріангуляція нових точок
            new_pts_prev, new_pts_curr, new_matches = [], [], []
            for m in good:
                if prev_view['kp_to_3d'][m.queryIdx] == -1:
                    new_pts_prev.append(prev_view['kp'][m.queryIdx].pt)
                    new_pts_curr.append(current_view['kp'][m.trainIdx].pt)
                    new_matches.append(m)

            if len(new_pts_prev) > 0 and current_view['P_ext'] is not None:
                p_prev_n = config.K_INV @ utils.cart2hom(np.array(new_pts_prev))
                p_curr_n = config.K_INV @ utils.cart2hom(np.array(new_pts_curr))
                new_tri = triangulation.linear_triangulation(p_prev_n, p_curr_n, prev_view['P_ext'],
                                                             current_view['P_ext'])
                for idx in range(new_tri.shape[1]):
                    if new_tri[2, idx] > 0:
                        all_points_3d.append(new_tri[:3, idx])
                        current_view['kp_to_3d'][new_matches[idx].trainIdx] = len(all_points_3d) - 1

        views.append(current_view)
        print(f"[{i}] Оброблено. Точок в хмарі: {len(all_points_3d)}")

    points_3d_np = np.array(all_points_3d)
    colors_np = colors.extract_colors(views, img_files, points_3d_np)
    cam_path = np.array([utils.get_camera_center(v['P_ext']) for v in views if v['P_ext'] is not None])

    visualization.visualize_sfm(points_3d_np, colors_np, cam_path)


if __name__ == "__main__":
    main()