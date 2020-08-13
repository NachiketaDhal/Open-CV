import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)     # 0-> Black
# print(img.shape)
# img[:] = 255, 0, 0

cv2.line(img, (0, 0), (512, 512), (0, 255, 0), 3)   # (img, pt1, pt2, color, thickness)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)  # (img, pt1, pt2, color, thickness/cv2.FILLED)
cv2.circle(img, (400, 50), 37, (255, 255, 0), 9)    # (img, center, radius, color, thickness)
cv2.putText(img, "OPEN CV", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)    # (img, text, starting point, font, scale, color, thickness)



cv2.imshow('Image', img)


cv2.waitKey(0)