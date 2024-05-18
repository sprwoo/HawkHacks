import cv2

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
file_name = "imgs/stockimg.jpg"

img = cv2.imread(file_name)
#img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)

cv2.imshow('img', img)
k = cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

i = 0
for (x, y, w, h) in faces:
    #cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,0), 2)
    cropped_image = gray[y : y + h, x : x + w]
    target_file_name = 'stored-faces/' + str(i) + '.jpg'
    cv2.imwrite(target_file_name, cropped_image)
    i += 1
