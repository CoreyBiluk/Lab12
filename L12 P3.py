# EETG 3024 Advanced Embedded Systems
# Instructor: Ricardo Bautista Quintero
# Corey Biluk | W0425561
# Lab 12 | Part 3
# April 4, 2021

import numpy as np
import cv2 as cv
import sys
# Imports first pic
img1 = cv.imread('Person 1.jpg')
# Import second pic
img2 = cv.imread('Person 1 moved.jpg')
# Resize first pic
img1 = cv.resize(img1, None, fx=0.15, fy=0.15, interpolation=cv.INTER_CUBIC)
# Resize second pic
img2 = cv.resize(img2, None, fx=0.15, fy=0.15, interpolation=cv.INTER_CUBIC)
# Sets how much of each pic is present. 0.5 is both equally
alpha = 0.5
# Calculates the weighted sum of two arrays
dst = cv.addWeighted(img1, 1 - alpha, img2, alpha, 0)
# show blended pic
cv.imshow('Dst', dst)
# Wait for key press
cv.waitKey(0)
# Close App
cv.destroyAllWindows()