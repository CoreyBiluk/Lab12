# EETG 3024 Advanced Embedded Systems
# Instructor: Ricardo Bautista Quintero
# Corey Biluk | W0425561
# Lab 12 | Part 1
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
# Show Image on screen
cv.imshow('Demo Image', res)
# Wait for key press
cv.waitKey(0)
# Close app
cv.destroyAllWindows()