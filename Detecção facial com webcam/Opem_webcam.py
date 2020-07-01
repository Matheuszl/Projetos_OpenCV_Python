import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

#carrega os arquivos de video de face e olhos
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

#looping infinito para atualizar o frame da cemara 
while True:
    _, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.25, 5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        cv.imshow("roi_gray", roi_gray)
        roi_color = frame[y:y+h, x:x+w]
        #cv.imshow("roi_color", roi_color)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == 27:
        break

video.release()
cv.destroyAllWindows()