import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('dataset.csv')
print(df.head())

plt.figure(figsize=(8,5))
plt.hist(df["keypoints"], bins=20)
plt.title("distribution of keypoints")
plt.xlabel("number of keypoints")
plt.ylabel("number of images")
plt.tight_layout()
plt.savefig("results/hist_keypoints.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["processing_time"], bins=20)
plt.title("distribution of processing time")
plt.xlabel("processing time (s)")
plt.ylabel("number of images")
plt.tight_layout()
plt.savefig("results/hist_processing_time.png")
plt.show()

plt.figure(figsize=(6,5))
plt.boxplot(df["matches"])
plt.title("boxplot of feature matches")
plt.ylabel("matches")
plt.tight_layout()
plt.savefig("results/boxplot_matches.png")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["blur"], df["keypoints"])
plt.xlabel("blur (variance of Laplacian)")
plt.ylabel("detected keypoints")
plt.title("blur vs keypoints")
plt.tight_layout()
plt.savefig("results/scatter_blur_keypoints.png")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["matches"], df["processing_time"])
plt.xlabel("matches")
plt.ylabel("processing time (s)")
plt.title("matches vs processing time")
plt.tight_layout()
plt.savefig("results/scatter_matches_time.png")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["matches"], df["new_points"])
plt.xlabel("matches")
plt.ylabel("new 3D points")
plt.title("matches vs new 3D points")
plt.tight_layout()
plt.savefig("results/scatter_matches_points.png")
plt.show()



