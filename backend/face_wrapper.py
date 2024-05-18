from backend.face_recognition import *
import os

def delete_files(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            os.remove(path)

def compare(group_photo):
    # Take group_photo from frontend
    
    # Replace this with a call to the database
    db_directory = "db" # From the database


    # Used to make local folder
    temp_directory = "./tmp_faces" 
    os.mkdir(temp_directory)

    # Get all faces in group_photo
    num_files = find_faces(temp_directory, group_photo)

    # Iterate through every face in the temporary folder
    for face in range(0, num_files):
        # Get file path
        group_face = temp_directory + "/" + str(face) + ".jpg"
        
        '''img = cv2.imread(group_photo)
        cv2.imshow("img", img)
        cv2.waitKey(0)'''

        # Compare faces
        found, db_face = compare_faces(db_directory, group_face)
        if found:
            print("Found!")
            print(group_face)
            print(db_face)
            print("\n")
    delete_files(temp_directory)
    os.rmdir(temp_directory)
    
compare("imgs/IMG_0276.jpg")