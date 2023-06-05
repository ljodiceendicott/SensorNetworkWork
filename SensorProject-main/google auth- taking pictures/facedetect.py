#Source:https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/?completed=/mog-background-reduction-python-opencv-tutorial/
import numpy as np
import cv2
import os

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haaracascade_face.xml')

cap = cv2.VideoCapture(0) 

# while(True):
#     cv2.imshow('img1',frame) #display the captured image
#     if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
#         cv2.imwrite('c1.png',frame)
#         cv2.destroyAllWindows()
#         break

# cap.release()

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    x = 0
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        roi_text = img[y:y+h, x:x+w]
        x = x +1
        if(x%300==5):
            ret,frame = cap.read()
            name = 'c1'+str(x)+'.png'
            cv2.imwrite(name,frame)
        

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()