from face_recognition import *
import os

def delete_files(directory: str) -> None:
    '''Deletes every file within a given directory path'''
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            os.remove(path)

def compare(group_photo: str) -> None:
    '''Given the path to a group photo, it finds every face using face_recognition.py, then
    attempts to find the face in the database. If successful, it sends the group photo to
    the associate email.'''
    # Take group_photo from frontend
    
    # Replace this with a call to the database
    db_directory = "group_images" # From the database


    # Used to make local folder which we will use to store faces found in the image
    temp_directory = "./tmp_faces" 
    os.mkdir(temp_directory)

    # Get all faces in group_photo
    num_files = find_faces(temp_directory, group_photo)

    # Iterate through every face in the temporary folder
    for face in range(0, num_files):
        # Get file path
        group_face = temp_directory + "/" + str(face) + ".jpg"
        
        # Debugging purposes
        '''img = cv2.imread(group_photo)
        cv2.imshow("img", img)
        cv2.waitKey(0)'''

        # Compare faces
        found, db_face = compare_faces(db_directory, group_face)
        if found:
            print("Found, " + group_face + " " + db_face + "\n")

    # Delete the temporary files
    delete_files(temp_directory)
    os.rmdir(temp_directory)

# Testing
compare("imgs/IMG_0276.jpg")