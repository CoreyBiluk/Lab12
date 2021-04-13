# EETG 3024 Advanced Embedded Systems
# Instructor: Ricardo Bautista Quintero
# Corey Biluk | W0425561
# Lab 12 | Part 2
# April 4, 2021

import numpy as np
import cv2 as cv
# Capture video frames
cap = cv.VideoCapture(0)
# Error check and message. exit program if error
if not cap.isOpened():
    print('Camera Error')
    exit()
# loop to display the video
while True:
    # Read the video frame.  ret is boolean T/F
    ret, frame = cap.read()
    # If ret is false. display error message and break
    if not ret:
        print('Error retrieving frame. Exiting...')
        break
    # Convert color video to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Show grayscale images
    cv.imshow('Demo Vid - Grayscale', gray)
    # Show color images
    cv.imshow('Demo Vid - Color', frame)
    # If 'q' is pressed, break
    if cv.waitKey(1) == ord('q'):
        break
# Releases the capture
cap.release()
# Close App
cv.destroyAllWindows()