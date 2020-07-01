import numpy as np
import cv2 as cv

image_path ='img_dark.jpg'
cascade_path = 'haarcascade_frontalface_default.xml'

clf = cv.CascadeClassifier(cascade_path)
img = cv.imread(image_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = clf.detectMultiScale(gray,1.25,10)

for (x,y,w,h) in faces:
    img = cv.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
