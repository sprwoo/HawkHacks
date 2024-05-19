from face_recognition import *
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def delete_files(directory: str) -> None:
    '''Deletes every file within a given directory path'''
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            os.remove(path)

def send_email(address: str) -> None:
    '''Uses SendGrid to send an email to address'''
    message = Mail(
        from_email = 'hr8patel@uwaterloo.ca',
        to_emails = address,
        subject = 'Sending with Twilio SendGrid is Fun',
        html_content = '<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

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
            print("Found! " + group_face + "; " + db_face + "\n")
            # send email

            send_email()

            '''img = cv2.imread(group_photo)
            img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
            cv2.imshow("img", img)
            cv2.waitKey(0)'''

    # Delete the temporary files
    delete_files(temp_directory)
    os.rmdir(temp_directory)

# Testing
compare("imgs/IMG_0276.jpg")