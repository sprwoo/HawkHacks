import cv2

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
file_name = "IMG_0276.jpg"

img = cv2.imread(file_name)
smaller_img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)
gray = cv2.cvtColor(smaller_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

i = 0
for (x, y, w, h) in faces:
    cropped_image = gray[y : y + h, x : x + w]
    target_file_name = 'stored-faces/' + str(i) + '.jpg'
    cv2.imwrite(target_file_name, cropped_image)
    i += 1
