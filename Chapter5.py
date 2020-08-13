import cv2
import numpy as np

img = cv2.imread('Resources/cards2.jpg')

width, height = 250, 350
pt1 = np.float32([[183, 24], [237, 75], [108, 106], [161, 159]])
pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pt1, pt2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
# print(imgOutput.shape)
# imgOutput = cv2.resize(imgOutput, (150, 250))



cv2.imshow('Image', img)
cv2.imshow('Output', imgOutput)

cv2.waitKey(0)
