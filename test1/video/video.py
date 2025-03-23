import cv2 as cv
import numpy as np
kernel =np.ones((5,5),np.uint8)
cap = cv.VideoCapture("video.mp4")
count = 0
object_detected = False
while True:
    c1 = 0
    ret,frame =cap.read()
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    tresh,result=cv.threshold(hsv_frame,180,255,cv.THRESH_BINARY_INV)
    grey_img = cv.cvtColor(result,cv.COLOR_BGR2GRAY)
    tresh,result1=cv.threshold(grey_img,180,255,cv.THRESH_TRUNC)
    _,result2=cv.threshold(result1,180,255,cv.THRESH_TOZERO_INV)
    _,result3=cv.threshold(result2,180,255,cv.THRESH_OTSU)
    dilation = cv.dilate(result3,kernel,2)
    open= cv.morphologyEx(dilation,cv.MORPH_OPEN,kernel,2)
    dilation1 = cv.dilate(open,kernel,2)
    tresh,result4=cv.threshold(dilation1,180,255,cv.THRESH_BINARY_INV)
    dilation2 = cv.dilate(result4,kernel,2)
    contour,hier = cv.findContours(dilation2,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    for con in contour:
        if 4300<cv.contourArea(con) <5500:
            draw_contour=cv.drawContours(frame,contour,-1,(0,255,0),2)
            c1 += 1
    if c1 > 0:
        if not object_detected:
            count += 1
            object_detected = True
    else:
        object_detected = False
    cv.putText(frame,str(count),(50,50),cv.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
    if ret:
        cv.imshow("frame",frame)
        cv.imshow("e",result4)
        if cv.waitKey(30) & 0xFF == ord("q"):
            break
cv.destroyAllWindows()