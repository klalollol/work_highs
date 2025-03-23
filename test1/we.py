import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# img = cv.imread("crop_coin.jpg")
# gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
 
 
# sobelx = cv.Sobel(img,-1,1,0)
# sobely = cv.Sobel(img,-1,0,1)
# sobelxy = cv.bitwise_or(sobelx,sobely)
# laplacian = cv.Laplacian(gray,-1)
# canny = cv.Canny(img,50,200)
 
# image = [img,sobelx,sobely,sobelxy,laplacian,canny]
# title = ["Original","SobelX","SobelY","SobelXY","Lapalcian","Canny"]
 
# for i in range(len(image)):
#     plt.subplot(2,3,i+1)
#     plt.imshow(image[i],cmap="gray")
#     plt.title(title[i])
#     plt.xticks([]),plt.yticks([])
 
# plt.show()
knl1 = np.ones((5, 5), np.uint8)
knl2 = np.ones((3, 3), np.uint8)
img1 = cv.imread("EE.jfif")
yellow_u = np.array([200,228,255])
yellow_d = np.array([141,187,251])
mask_yellow = cv.inRange(img1,yellow_d,yellow_u)
dilate_y = cv.dilate(mask_yellow,kernel=knl1,iterations=1)
 
 
white_u = np.array([255,255,255])
white_d = np.array([235,235,235])
mask_white = cv.inRange(img1,white_d,white_u)
closing = cv.morphologyEx(mask_white, cv.MORPH_CLOSE, knl1, iterations=5)
erosion = cv.erode(closing, knl2, iterations=1)
dilate_w = cv.dilate(erosion,kernel=knl2,iterations=8)
 
 
 
 
 
masked = cv.bitwise_or(dilate_w,dilate_y)
mask_img = cv.bitwise_and(img1,img1,mask = masked)
blur_img = cv.GaussianBlur(mask_img,(5,5),0)
 
grey = cv.cvtColor(blur_img,cv.COLOR_BGR2GRAY)
edge = cv.Canny(grey,10,150,apertureSize=3)
line = cv.HoughLinesP(edge,1,np.pi/180,200,minLineLength=1,maxLineGap=10000)
# line = cv.HoughLines(edge,1,np.pi/180,200)
 
for i in line:
    # rho , theta = i[0]
    # a = np.cos(theta)
    # b = np.sin(theta)
    # x0 = a*rho
    # y0 = b*rho
    # x1 = int(x0 +1000*(-b))
    # y1 = int(y0 +1000*(a))
    # x2 = int(x0 -1000*(-b))
    # y2 = int(y0 -1000*(a))
 
    x1,y1,x2,y2 = i[0]
    cv.line(img1,(x1,y1),(x2,y2),(0,255,0),2)
 
cv.imshow("E",dilate_w)
cv.imshow("canny",edge)
cv.imshow("line",img1)
cv.waitKey(0)
cv.destroyAllWindows()