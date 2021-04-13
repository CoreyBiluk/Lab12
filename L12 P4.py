# EETG 3024 Advanced Embedded Systems
# Instructor: Ricardo Bautista Quintero
# Corey Biluk | W0425561
# Lab 12 | Part 4
# April 4, 2021

import cv2 as cv
import sys
# Import image from folder
img = cv.imread('Demo pic.jpg')
# Resize image
res = cv.resize(img, None, fx=0.15, fy=0.15, interpolation=cv.INTER_CUBIC)
# Error message if not image is present in folder
if img is None:
    sys.exit('Error loading image')
# Creates a file of a picture of the edges in the original picture
cv.imwrite("Canny.jpg",cv.Canny(res,200, 300))
# Load new canny image
img2 = cv.imread('Canny.jpg')
# Show canny image
cv.imshow('Demo Image', img2)
# Wait for key press
cv.waitKey(0)
# Close app
cv.destroyAllWindows()