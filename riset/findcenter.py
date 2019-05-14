import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
field_image = np.copy(image)
gray = cv2.cvtColor(field_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (9,9),0)
outline =cv2.Canny(blur, 50, 150)

#Hough Line Transform Probabilistic
lines = cv2.HoughLinesP(outline, 1, np.pi/180,100,minLineLength=100,maxLineGap=50)

for line in lines:
	x1,y1,x2,y2 = line[0]
	cv2.line(image, (x1,y1), (x2,y2),(0,0,255),3)

#Hough Line Transform	
"""
lines = cv2.HoughLines(outline,1,np.pi/180,100)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
"""
cv2.imshow("outline", outline)
cv2.imshow("result",image)
cv2.waitKey(0)
