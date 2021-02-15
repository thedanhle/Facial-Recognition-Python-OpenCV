import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #loading classifier

img = cv2.imread('pattern.png') #load the sample image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert img to gray scale (blue green red to gray)

faces = face_cascade.detectMultiScale(gray, 1.1, 4) #detect face

for(x, y, w, h) in faces:                                          #facial coordinates
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)    #draw a rectangle on face

cv2.imshow('img', img)
cv2.waitKey()
