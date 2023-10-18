import numpy as np
import cv2

cap=cv2.VideoCapture(0)

green_lower_range=np.array([40,100,160])
green_upper_range=np.array([65,160,205])

red_lower_range=np.array([0,175,255])
red_upper_range=np.array([179,215,255])

yellow_lower_range=np.array([11,120,255])
yellow_upper_range=np.array([25,165,255])

def green(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,green_lower_range,green_upper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("GREEN"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

def red(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,red_lower_range,red_upper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,("RED"),(10,100),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

def yellow(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,yellow_lower_range,yellow_upper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(frame,("YELLOW"),(10,140),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    green(frame)
    red(frame)
    yellow(frame)
            
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
