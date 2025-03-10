import cv2 as cv
import numpy as np
a = False
kernel = np.ones((3,3),np.uint8)
cap  = cv.VideoCapture("videoplayback.mp4")
while (cap.isOpened()):
    ret , frame = cap.read()
    if a == True:
        grey_cap_copy = grey_cap.copy()
    if ret == True:
        grey_cap = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
        a = not a
        if a ==False:
          diff = cv.absdiff(grey_cap,grey_cap_copy)
          blur = cv.GaussianBlur(diff,(5,5),0)
          tresh,result= cv.threshold(blur,50,255,cv.THRESH_BINARY)
          dilation = cv.dilate(result,None,iterations =3)
          contours,hier = cv.findContours(dilation,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
          draw_con = cv.drawContours(frame,contours,-1,(0,0,255),2)
          for contour in contours:
            (x,y,w,h) = cv.boundingRect(contour)
            if cv.contourArea(contour) <2500:
                  continue
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
            cv.putText(frame,"detect",(0,50),cv.FONT_HERSHEY_DUPLEX,2,(255,255,255),5)
        else:
            continue
        cv.imshow("Frame",frame)
        cv.imshow("vid",diff)
        if cv.waitKey(30) == ord("q"):
            break
cap.release()
cv.destroyAllWindows()