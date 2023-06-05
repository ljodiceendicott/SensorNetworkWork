#Source:https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/?completed=/mog-background-reduction-python-opencv-tutorial/
import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haaracascade_face.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_glasses.xml
eye_cascade = cv2.CascadeClassifier('haaracascade_glasses.xml')

# smile_cascade = cv2.CascadeClassifier('haaracascade_smile.xml')

hand_cascade = cv2.CascadeClassifier('haaracascade_hand.xml')

cap = cv2.VideoCapture(0) 

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

    for (hx,hy,hw,hh) in hands:
        cv2.rectangle(img,(hx,hy),(hx+hw,hy+hh),(0,0,255),4)
        cv2.putText(img,"hand-Detected",(x,y), font, .5, (1,1,1), 2, cv2.LINE_AA)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        roi_text = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        num_eyes = 0
        for (ex,ey,ew,eh) in eyes:
            num_eyes = num_eyes + 1
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'eye',(ex+x,ey+y), font, .4, (30,30,30), 2, cv2.LINE_AA) 

        # smile = smile_cascade.detectMultiScale(roi_gray)
        # for(sx,sy,sw,sh) in smile:
        #     cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        #status should change based on the eyse that are given
        status = ''
        if num_eyes == 1 :
            ##you blinked
            status = 'wink/ One eye closed'
        elif num_eyes ==0:
            status = 'blink/No eyes Detected'
        elif num_eyes ==2:
            status = 'Both eyes open'
        eye_status = 'Eyes status:'+ status
       
        cv2.putText(img,eye_status,(x,y), font, .5, (1,1,1), 2, cv2.LINE_AA)
        

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()