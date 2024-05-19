import cv2
import os
from deepface import DeepFace
from typing import Tuple

def find_faces(directory: str, group_photo: str) -> int:
    '''directory and group_photo are both strings that represent a path. directory is the
    the landing location of the faces we find in group_photo. find_faces() uses OpenCV and haarcascade
    to find the positions of faces and store them in the directory. It returns an int representing the number
    of faces it found. '''
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    #file_name = "imgs/IMG_0022.jpg"

    # Read the image
    image = cv2.imread(group_photo)
    
    # Testing purposes
    #img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)
    '''cv2.imshow('img', image)
    cv2.waitKey(0)'''

    # Grayscale then use the haar cascade algorithm
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # Crop out the locations of the faces found then save to directory
    num = 0
    for (x, y, w, h) in faces:
        #cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,0), 2)
        cropped_image = gray[y : y + h, x : x + w]
        target_file_name = directory + '/' + str(num) + '.jpg'
        cv2.imwrite(target_file_name, cropped_image)
        num += 1

    return num

def compare_faces(db_directory: str, group_face: str) -> Tuple[bool, str]:
    '''Given strings, db_directory and group_face, which represent paths to a location, 
    we return a boolean depending on if group_face can be found in the directory. compare_faces() uses
    DeepFace to verify if two faces are similar. '''

    # Loop through database
    for face in os.listdir(db_directory):
        # Make path to database face
        filename = os.fsdecode(face)
        reference_picture = os.path.join(db_directory, filename)

        # DeepFace to check similarity
        result = DeepFace.verify(img1_path = group_face, img2_path = reference_picture, enforce_detection=False)
        if result['verified']:
            return True, reference_picture
    return False, None