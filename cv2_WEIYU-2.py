import cv2
import numpy as np
import pytesseract as pt

import os



m1 = cv2.imread("C:\python\opencv\WEIYU-2.png",1)
m2=cv2.erode(m1,np.ones((25,25)))
m2=cv2.cvtColor(m2,cv2.COLOR_BGR2GRAY)
t,m2=cv2.threshold(m2,240,255,cv2.THRESH_BINARY)
m2=cv2.bitwise_not(m2)
p,t=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for d in p:
    x,y,w,h = cv2.boundingRect(d)
    if w>h+10:
        m2=m1[y:y+h,x:x+w].copy()
        m1[:,:]=255
        m1[y:y+h,x:x+w]=m2

cv2.imshow("im1",m1)
t=pt.image_to_string(m1,'eng')
print(t)


cv2.waitKey(0)
cv2.destroyAllWindows()
