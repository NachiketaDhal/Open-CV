import cv2
import numpy as np

vid = cv2.VideoCapture(0)
vid.set(3, 640)     # Frame width
vid.set(4, 480)     # Frame height
vid.set(10, 150)    # Brightness

myColors = [[0, 163, 136, 130, 255, 255]]   # h_min, s_min, v_min, h_max, s_max, v_max
myColorValues = [[255, 0, 0]]       # BGR format of the chosen color

myPoints = []       # x, y, color id to draw the colors (point[0], point[1], point[2])


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0   # To match the color of the circle at the tip with the corresponding color in myColorValues
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])     # For loop to apply multiple colors
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)  # If we move track bar the image changes
        x, y = getcontours(mask)
        cv2.circle(imgResult, (x, y), 7, myColorValues[count], cv2.FILLED)  # To draw the circle in center of the tip
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    # cv2.imshow('Result str(color[0])', mask)
    return newPoints
def getcontours(img):  # Function to find out the contour
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)   # To find the contour
    x, y, w, h = 0, 0, 0, 0     # In case area is less than 500 it will return something
    for cnt in contours:
        area = cv2.contourArea(cnt)     # Area of the shapes
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (0, 0, 0), 2)  # Draws the contours of the different shapes
            peri = cv2.arcLength(cnt, True)     # To find the perimeter
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)    # To count the number of corners in contour
            x, y, w, h = cv2.boundingRect(approx)  # To get the bounding boundary of  x, y, w, h of each shape
    return x+w//2, y    # Center of the tip detection

def drawOn(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 7, myColorValues[point[2]], cv2.FILLED)



while True:
    success, img = vid.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOn(myPoints, myColorValues)

    cv2.imshow('Video', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
