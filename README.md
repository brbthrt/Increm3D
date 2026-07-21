# Incremental 3D Reconstruction and Data Analysis

This project implements an incremental Structure from Motion (SfM) pipeline for 3D object reconstruction from multiple images using Python, OpenCV, and Open3D. 
In addition to the reconstruction pipeline, the project performs data collection, exploratory data analysis (EDA), statistical analysis, and PostgreSQL integration.

<p align="center">
  <img src="img/dino_far.png" alt="3D Reconstruction" width="550">
</p>

[//]: # (The program:)

[//]: # (- detects and matches image features using SIFT,)

[//]: # (- estimates camera motion,)

[//]: # (- triangulates 3D points,)

[//]: # (- incrementally reconstructs a sparse 3D scene,)

[//]: # (- visualizes the reconstructed point cloud and mesh.)

---

# Features

## 3D Reconstruction

- SIFT feature detection and matching
- Essential matrix estimation
- Camera pose recovery
- Incremental PnP camera localization
- Linear triangulation
- Reprojection error analysis
- Colored point cloud generation
- 3D visualization with Open3D
- Mesh reconstruction using Alpha Shapes
- 

## Data Collection

- image resolution
- number of detected keypoints
- number of feature matches
- image blur (variance of Laplacian)
- image brightness
- image contrast
- processing time
- reprojection error
- number of newly reconstructed 3D points
These metrics are exported to dataset.csv.

---

# Exploratory Data Analysis

The project performs exploratory data analysis using **Pandas**, **Matplotlib**, and **Seaborn**.

Implement analyses include:
- Descriptive statistics
- Histograms
- Scatter plots
- Boxplots
- Correlation matrix
- Quartile analysis

Generated visualization:
- Distribution of detected keypoints
- Distribution of processing time
- Feature matches boxplot
- Blur vs processing time
- Matches vs reconstructed 3D points
- Correlation matrix

---

# PostgreSQL Integration

The generated dataset can be imported into PostgreSQL.

The project includes:

- CSV loading
- Automatic insertion into PostgreSQL
- Environment variables using `.env`
- Secure database connection with `python-dotenv`

---

# Project Structure

```text
Increm3D/
│
├── img/
│
├── data_analysis/
│   ├── analysis.py
│   ├── dataset_statistics.py
│   ├── correlation_matrix.py
│   ├── database.py
│   └── results/
│
├── colors.py
├── config.py
├── features.py
├── triangulation.py
├── utils.py
├── visualization.py
├── main.py
├── main_with_errors.py
├── dataset.csv
├── reconstruction_stats.png
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies

- Python
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Seaborn
- PostgreSQL
- psycopg2
- Open3D

---

# Installation

## 1. Clone repository

## 2. Create virtual environment 

## 3. Install dependencies 'requirements.txt'

## 4. Run the project 

---

# How the Pipeline Works

## 1. Feature Detection
SIFT is used to detect keypoints and descriptors for every image.

## 2. Feature Matching
FLANN-based matcher performs nearest-neighbor matching between consecutive frames.

## 3. Initial Reconstruction
For the first image pair:
- the Essential matrix is estimated
- camera pose is recovered
- initial 3D points are triangulated

## 4. Incremental Reconstruction
For every next frame:
- camera pose is estimated using PnP
- new 3D points are triangulated
- reconstructed scene grows incrementally

## 5. Error Estimation
The reprojection error is computed for evaluating reconstruction quality.

## 6. Dataset Generation
For every processed image, the following metrics are collected:

- image resolution;
- number of detected keypoints;
- number of feature matches;
- blur (Variance of Laplacian);
- brightness;
- contrast;
- processing time;
- reprojection error;
- number of newly reconstructed 3D points.

The collected information is exported to **dataset.csv**.

## 7. Compute reconstruction quality metrics.
The generated dataset is analyzed using **Pandas**, **Matplotlib**, and **Seaborn**.

The analysis includes:

- descriptive statistics;
- histograms;
- boxplots;
- scatter plots;
- correlation matrix.


## 8. Database Integration
The generated dataset is imported into a PostgreSQL database for structured storage and further analysis.

## 9. Visualization
The reconstruction pipeline produces:

- sparse 3D point cloud;
- reconstructed mesh;
- reconstruction statistics;
- analytical charts.

## 10. Store the dataset in PostgreSQL.

---

# Dataset Description

| Feature | Description |
|----------|-------------|
| image | Image filename |
| width | Image width |
| height | Image height |
| keypoints | Number of detected keypoints |
| matches | Number of feature matches |
| blur | Image blur (Variance of Laplacian) |
| brightness | Average pixel intensity |
| contrast | Standard deviation of pixel intensities |
| processing_time | Processing time (seconds) |
| reprojection_error | Average reprojection error |
| new_points | Number of newly reconstructed 3D points |

---

# Input Data

Place input images inside:

```text
img/
```

Dataset:
https://www.robots.ox.ac.uk/~vgg/data/mview/
Supported formats:
- `.jpg`
- `.png`
- `.ppm`

---

# Camera Intrinsic Matrix

Camera calibration matrix is defined in `config.py`:

---

# Output

The program generates:
- sparse 3D point cloud
- reconstructed mesh
- reprojection error graph
- Reconstruction statistics
- CSV dataset
- Descriptive statistics
- Histograms
- Scatter plots
- Boxplots
- Correlation matrix
- PostgreSQL database records

Saved directory:

```text
data_analysis/results
```

---

# Author

Roksolana Savuliak  
Applied Mathematics Student