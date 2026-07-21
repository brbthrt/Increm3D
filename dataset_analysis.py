import cv2
import numpy as np

def calculate_blur(gray):
    # variance of the Laplacian is used as a blur metric
    # higher values indicate a sharper image
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def calculate_brightness(gray):
    # average pixel intensity (0-255)
    return np.mean(gray)

def calculate_contrast(gray):
    # standard deviation of pixel intensities
    # higher values correspond to higher contrast
    return np.std(gray)