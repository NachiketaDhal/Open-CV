# Face detection
import cv2

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
img = cv2.imread('Resources/lena.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)   # Detects the face
for (x, y, w, h) in faces:
    cv2.rectangle(imgGray, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draws a rectangle around the face

cv2.imshow('Result', imgGray)
cv2.waitKey(0)