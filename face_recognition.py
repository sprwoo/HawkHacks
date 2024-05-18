import cv2
import os
from deepface import DeepFace

def find_faces(directory, group_photo):
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    #file_name = "imgs/IMG_0022.jpg"

    img = cv2.imread(group_photo)
    #img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)
    '''cv2.imshow('img', img)
    k = cv2.waitKey(0)'''

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)

    num = 0
    for (x, y, w, h) in faces:
        #cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,0), 2)
        cropped_image = gray[y : y + h, x : x + w]
        target_file_name = directory + '/' + str(num) + '.jpg'
        cv2.imwrite(target_file_name, cropped_image)
        num += 1
    return num

def compare_faces(db_directory, group_face):
    for face in os.listdir(db_directory):
        filename = os.fsdecode(face)
        reference_picture = os.path.join(db_directory, filename)
        result = DeepFace.verify(img1_path = group_face, img2_path = reference_picture, enforce_detection=False)
        if result['verified']:
            return True, reference_picture
    return False, None