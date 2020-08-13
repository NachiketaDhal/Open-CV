import cv2
print('Package Imported')

img = cv2.imread('Resources/test.jpg')
cv2.imshow('Output', img)
cv2.waitKey(0)

