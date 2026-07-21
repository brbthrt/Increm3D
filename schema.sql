CREATE TABLE Images
(
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    width INTEGER,
    height INTEGER,
    keypoints INTEGER,
    matches INTEGER,
    blur DOUBLE PRECISION,
    brightness DOUBLE PRECISION,
    contrast DOUBLE PRECISION,
    processing_time DOUBLE PRECISION,
    reprojection_error DOUBLE PRECISION,
    new_points INTEGER
);