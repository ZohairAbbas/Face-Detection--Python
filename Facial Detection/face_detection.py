import cv2
import numpy as np
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

# This code is able to detect multiple faces in real time
cap = cv2.VideoCapture(0)

while 3:
        ret, img = cap.read()
        img = cv2.flip( img, 1 )
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        
        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                cv2.putText(img,'Face Detected',(x+20,y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2, cv2.LINE_AA) 
                               
        cv2.imshow('img',img)
        if cv2.waitKey(1) == ord('q'):
            break
            
cap.release()
cv2.destroyAllWindows()
