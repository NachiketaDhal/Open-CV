import cv2
import numpy as np

img = cv2.imread('Resources/test.jpg')
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # Converts to gray image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)      # Converts to blurred image
imgCanny = cv2.Canny(img, 100, 100)     # Detects the edge of the image
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)    # Makes the edge thicker
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)    # Makes the edge thinner

cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilation Image', imgDilation)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)