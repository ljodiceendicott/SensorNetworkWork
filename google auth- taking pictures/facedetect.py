#Source:https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/?completed=/mog-background-reduction-python-opencv-tutorial/
import numpy as np
import cv2
import os

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haaracascade_face.xml')

cap = cv2.VideoCapture(0)

print("Which would you like to capture? \n-(2.)Video\n-(1.)Photo")
cap_type =input()
#https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
width = int(cap.get(3))
height = int(cap.get(4))
if(cap_type == '2'):
    out = cv2.VideoWriter('evidence.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 60, (width,height))
   
# while(True):
#     cv2.imshow('img1',frame) #display the captured image
#     if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
#         cv2.imwrite('c1.png',frame)
#         cv2.destroyAllWindows()
#         break

# cap.release()

while cv2.waitKey(30) & 0xff != ord('c'):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if(cap_type == '1'):
        x = 0
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            roi_text = frame[y:y+h, x:x+w]
            x = x +1
            if(x%300==5):
                ret,frame = cap.read()
                # name = 'G:\My Drive\caughtimages\c1'+str(x)+'.png'
                name = str(x)+'.png'
                cv2.imwrite(name,frame)
    elif(cap_type == '2'):
    #    while cv2.waitKey(30) & 0xff != ord('q'):
            ret,frame = cap.read()
            if ret == True:
                out.write(frame)
                cv2.imshow("capture", frame)
            # if cv2.waitKey(30) & 0xff == ord('q'):
            #     break
            # elif cv2.waitKey(30) & 0xff == ord('x'):
            #     cap.release()
            #     cv2.destroyAllWindows()
            #     exit()


    cv2.imshow('frame',frame)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()