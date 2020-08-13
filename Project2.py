import cv2

vid = cv2.VideoCapture(0)
vid.set(3, 640)
vid.set(4, 480)
vid.set(10, 100)
minarea = 500
color = (255, 0, 255)
nPlateCascade = cv2.CascadeClassifier('Resources/haarcascade_russian_platenumber.xml')

while True:
    success, img = vid.read()
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(img, 1.1, 10)  # Detects the number plates
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minarea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)  # Draws a rectangle around the numplate
            cv2.putText(img, 'Number Plate', (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]      # Region of number plate pops up in another smaller window
            cv2.imshow('ROI', imgRoi)


    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

