# Contours and shape detection
import cv2
import numpy as np

def stackImages(scale,imgArray):        # Function to stack up multiple images
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getcontours(img):  # Function to find out the contour
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)   # To find the contour
    for cnt in contours:
        area = cv2.contourArea(cnt)     # Area of the shapes
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)  # Draws the contours of the different shapes
            peri = cv2.arcLength(cnt, True)     # To find the perimeter
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)    # To count the number of corners in contour
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)  # To get the bounding boundary of  x, y, w, h of each shape
            if objCor == 3:
                objectType = 'Tri'
            elif objCor == 4:
                aspRatio = float(w)/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = 'Square'
                else:
                    objectType = 'Rectangle'
            elif objCor == 5:
                objectType = 'Penta'
            elif objCor == 6:
                objectType = 'Hexa'
            elif objCor == 7:
                objectType = 'Septa'
            elif objCor == 8:
                objectType = 'Octa'
            else:
                objectType = 'None'



            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2) # To print a rectangle around the shapes
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)  # Name of the shape






img = cv2.imread('Resources/shapes2.jpg')       # Original image
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # Gray image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)  # Blurred image
imgCanny = cv2.Canny(imgBlur, 50, 50)     # To detect the outline of the image
getcontours(imgCanny)


# imgBlank = np.zeros_like(img)
imgBlank = np.zeros((512, 512, 3), np.uint8)
imgStack = stackImages(1, ([img, imgGray, imgBlur],
                           [imgCanny, imgContour, imgBlank]))   # Create stacks of images using the function



# cv2.imshow('Original', img)
# cv2.imshow('Gray', imgGray)
# cv2.imshow('Blur', imgBlur)
cv2.imshow('Stack', imgStack)

cv2.waitKey(0)