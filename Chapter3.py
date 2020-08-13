import cv2
import numpy as np

img = cv2.imread('Resources/test.jpg')
print(img.shape)

imgResize = cv2.resize(img, (200, 500))     # (width, height)
print(imgResize.shape)

imgCropped = img[50:600, 100:470]       # (height, width)
print(imgCropped.shape)     # (height, width)

cv2.imshow('Image', img)
cv2.imshow('Resized Image', imgResize)
cv2.imshow('Cropped Image', imgCropped)

cv2.waitKey(0)