# Number plate detection from images
import cv2

nPlateCascade = cv2.CascadeClassifier('Resources/haarcascade_russian_platenumber.xml')
img = cv2.imread('Resources/car3.jpg')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numberPlate = nPlateCascade.detectMultiScale(img, 1.1, 4)   # Detects the face
for (x, y, w, h) in numberPlate:
    area = w*h
    if area > 100:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)  # Draws a rectangle around the face
        cv2.putText(img, 'Number Plate', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)