import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frameX =cv2.GaussianBlur(frame,(5,5),0)
    hsv= cv2.cvtColor(frameX,cv2.COLOR_BGR2HSV)
    low_white = np.array([0,0,0])
    up_white = np.array([0,0,255])
    mask = cv2.inRange(hsv, low_white, up_white)
    edges = cv2.Canny(mask,75,150)

    lines = cv2.HoughLinesP(edges, 1,np.pi/180,50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(frameX,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow('frame',frameX)
    cv2.imshow("edges",edges)

    #cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()