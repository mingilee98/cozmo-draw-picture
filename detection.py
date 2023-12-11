import cv2
import numpy as np
from skimage import measure


def find_shape(file_path):
    # read and prerprfile_pathocess image
    img = cv2.imread(file_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)  # apply GaussianBlur

    # find edges
    edges = cv2.Canny(blurred, 50, 150)

    # find contours in the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    shape = None
    for contour in contours:
        # polygonal curves of the contour
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # get vertices and find shape
        vertices = len(approx)
        if vertices == 3:
            shape = "Triangle"
        elif vertices == 4:
            shape = "Rectangle"
        elif vertices == 5:
            shape = "Pentagon"
        elif vertices == 6:
            shape = "Hexagon"
        else:
            shape = "Circle"

    return shape


def find_path(file_path):
    pass
