import cv2
import numpy as np

img = cv2.imread('Resources/test.jpg')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))
# imgVer = cv2.resize(imgVer, (400, 600))


cv2.imshow('Image', img)
cv2.imshow('Horizontal', imgHor)
cv2.imshow('Vertical', imgVer)

cv2.waitKey(0)