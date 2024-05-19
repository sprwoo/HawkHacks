from face_recognition import *
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import aiohttp
import asyncio
import base64

def delete_files(directory: str) -> None:
    '''Deletes every file within a given directory path'''
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            os.remove(path)

def send_email(address: str, photo: str) -> None:
    '''Uses SendGrid to send an email to address'''
    message = Mail(
        from_email = 'hr8patel@uwaterloo.ca',
        to_emails = address,
        subject = 'Group photo!',
        html_content = 'Heyyyyy')
    
    with open(photo, 'rb') as f:
        data = f.read()
        encoded_file = base64.b64encode(data).decode()

    attached_file = Attachment(
        FileContent(encoded_file),
        FileName(os.path.basename(photo)),
        FileType('image/jpg'),  # You can change this to the appropriate file type
        Disposition('attachment')
    )
    message.attachment = attached_file
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        #print(response.status_code)
        #print(response.body)
        #print(response.headers)
    except Exception as e:
        print(e.message)

async def fetch_email(session, db_face):
    url = f'http://127.0.0.1:8000/pictures/{db_face}'
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return data.get('email')
        else:
            print(f"Failed to retrieve data: {response.status}")
            return None

async def process_face(session, db_directory, temp_directory, face, group_photo):
    group_face = os.path.join(temp_directory, f"{face}.jpg")
    found, db_face = compare_faces(db_directory, group_face)
    if found:
        print(f"Found! {group_face}; {db_face}\n")
        db_face = db_face[13:]
        email = await fetch_email(session, db_face)
        if email:
            send_email(email, group_photo)
            print("Worked!")
        else:
            print("Email not found in the response.")
    else:
        print(f"Face not found in the database for {group_face}")

async def compare(group_photo: str) -> None:
    db_directory = "group_images"  # Replace this with a call to the database
    temp_directory = "./tmp_faces"
    os.mkdir(temp_directory)

    num_files = find_faces(temp_directory, group_photo)

    async with aiohttp.ClientSession() as session:
        tasks = [process_face(session, db_directory, temp_directory, face, group_photo) for face in range(num_files)]
        await asyncio.gather(*tasks)

    delete_files(temp_directory)
    os.rmdir(temp_directory)

# To run the async function
def wrap(group_photo: str) -> None:
    asyncio.run(compare("img/IMG_0293"))

# def compare(group_photo: str) -> None:
#     '''Given the path to a group photo, it finds every face using face_recognition.py, then
#     attempts to find the face in the database. If successful, it sends the group photo to
#     the associate email.'''
#     # Take group_photo from frontend
    
#     # Replace this with a call to the database
#     db_directory = "group_images" # From the database


#     # Used to make local folder which we will use to store faces found in the image
#     temp_directory = "./tmp_faces" 
#     os.mkdir(temp_directory)

#     # Get all faces in group_photo
#     num_files = find_faces(temp_directory, group_photo)

#     # Iterate through every face in the temporary folder
#     for face in range(0, num_files):
#         # Get file path
#         group_face = temp_directory + "/" + str(face) + ".jpg"
        
#         # Debugging purposes
#         '''img = cv2.imread(group_photo)
#         cv2.imshow("img", img)
#         cv2.waitKey(0)'''

#         # Compare faces
#         found, db_face = compare_faces(db_directory, group_face)
#         if found:
#             print("Found! " + group_face + "; " + db_face + "\n")
#             # send email
#             db_face = db_face[13:]
#             result = requests.get('http://127.0.0.1:8000/pictures/' + db_face)

#             if result.status_code == 200:
#                 data = result.json()
#                 email = data.get('email')  # Replace 'email' with the actual key in your JSON response
                
#                 if email:
#                     send_email(email)
#                 else:
#                     print("Email not found in the response.")
#             else:
#                 print(f"Failed to retrieve data: {result.status_code}")
#             # requests.post('http://127.0.0.1:8000/send_email/')
            

#             '''img = cv2.imread(group_photo)
#             img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
#             cv2.imshow("img", img)
#             cv2.waitKey(0)'''

#     # Delete the temporary files
#     delete_files(temp_directory)
#     os.rmdir(temp_directory)

# Testing
#compare("imgs/IMG_0295.jpg")