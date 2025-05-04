import cv2
import numpy as np
import pytesseract as pt

m1=cv2.imread("C:\python\opencv\car.jpg", 1)
m2=m1.copy()
m2[:,:,0]=cv2.adaptiveThreshold(m1[:,:,0],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,0)
m2[:,:,1]=cv2.adaptiveThreshold(m1[:,:,1],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,0)
m2[:,:,2]=cv2.adaptiveThreshold(m1[:,:,2],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,0)
#cv2.imshow("Image M1", m2)
#cv2.waitKey(0)
m2=cv2.cvtColor(m2,cv2.COLOR_BGR2GRAY)
ct, th=cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
parentList=np.zeros((len(ct)))
for d in th[0]:
        if d[3]!=-1:
                parentList[d[3]]+=1


for d in np.where(parentList>9)[0]:
        x, y, w, h =cv2.boundingRect(ct[d])
        if w>h*1.2 and w<h*3:
                m2=m1[y:y+h,x:x+w].copy()
                m2=cv2.cvtColor(m2,cv2.COLOR_BGR2GRAY)
                m2=cv2.divide(m2,np.full(m2.shape,51,np.uint8))
                m2=cv2.multiply(m2,np.full(m2.shape,51,np.uint8))
                if len(np.where(m2>=204)[0])>m2.shape[0]*m2.shape[1]*0.2:
                        #cv2.imwrite("output/"+str(x)+".png", m1[y:y+h,x:x+w])
                        cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("Image M1", m1)

cv2.waitKey(0)
cv2.destroyAllWindows()
