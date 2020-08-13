# Color detection using webcam
import cv2
import numpy as np

vid = cv2.VideoCapture(0)
vid.set(3, 480)
vid.set(4, 360)
vid.set(10, 100)

def empty(a):
    pass



cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 240)
cv2.createTrackbar('Hue Min', 'Trackbar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'Trackbar', 19, 179, empty)
cv2.createTrackbar('Sat Min', 'Trackbar', 110, 255, empty)
cv2.createTrackbar('Sat Max', 'Trackbar', 240, 255, empty)
cv2.createTrackbar('Val Min', 'Trackbar', 153, 255, empty)
cv2.createTrackbar('Val Max', 'Trackbar', 255, 255, empty)

while True:



    _, img = vid.read()
        # cv2.imshow('Video', img)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'Trackbar')
    h_max = cv2.getTrackbarPos('Hue Max', 'Trackbar')
    s_min = cv2.getTrackbarPos('Sat Min', 'Trackbar')
    s_max = cv2.getTrackbarPos('Sat Max', 'Trackbar')
    v_min = cv2.getTrackbarPos('Val Min', 'Trackbar')
    v_max = cv2.getTrackbarPos('Val Max', 'Trackbar')
    # print(h_min, h_min, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)    # If we move trackbar the image changes
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, imgResult])
    cv2.imshow('Video', hstack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()





    # cv2.imshow('Original', img)
    # cv2.imshow('HSV', imgHSV)
    # cv2.imshow('Mask', mask)
    # cv2.imshow('Result', imgResult)



    # cv2.waitKey(1)