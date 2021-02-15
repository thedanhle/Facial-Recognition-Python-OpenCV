import cv2

face_cascade = cv2.CascadeClassifier()  # loading classifier

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()  # two variables; flags if read correctly and frame itself called img

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert img to gray scale (blue green red to gray)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # detect face

    for (x, y, w, h) in faces:  # facial coordinates
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # draw a rectangle on face

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()


