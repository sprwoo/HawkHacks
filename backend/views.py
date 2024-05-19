import os
import requests
import aiohttp
import asyncio
import base64
import cv2
from typing import Tuple
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Picture
from .serializers import PictureSerializer
from django.core.files.storage import default_storage
from deepface import DeepFace
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

def delete_files(directory: str) -> None:
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            os.remove(path)

def send_email(address: str, photo: str) -> None:
    message = Mail(
        from_email='hr8patel@uwaterloo.ca',
        to_emails=address,
        subject='Group photo!',
        html_content='Heyyyyy'
    )
    with open(photo, 'rb') as f:
        data = f.read()
        encoded_file = base64.b64encode(data).decode()

    attached_file = Attachment(
        FileContent(encoded_file),
        FileName(os.path.basename(photo)),
        FileType('image/jpg'),
        Disposition('attachment')
    )
    message.attachment = attached_file
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
    except Exception as e:
        print(e.message)

def find_faces(directory: str, group_photo: str) -> int:
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    image = cv2.imread(group_photo)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    num = 0
    for (x, y, w, h) in faces:
        cropped_image = gray[y:y + h, x:x + w]
        target_file_name = directory + '/' + str(num) + '.jpg'
        cv2.imwrite(target_file_name, cropped_image)
        num += 1
    return num

def compare_faces(db_directory: str, group_face: str) -> Tuple[bool, str]:
    for face in os.listdir(db_directory):
        filename = os.fsdecode(face)
        reference_picture = os.path.join(db_directory, filename)
        result = DeepFace.verify(img1_path=group_face, img2_path=reference_picture, enforce_detection=False)
        if result['verified']:
            return True, reference_picture
    return False, None

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
    db_directory = "group_images"
    temp_directory = "./tmp_faces"
    os.mkdir(temp_directory)
    num_files = find_faces(temp_directory, group_photo)
    async with aiohttp.ClientSession() as session:
        tasks = [process_face(session, db_directory, temp_directory, face, group_photo) for face in range(num_files)]
        await asyncio.gather(*tasks)
    delete_files(temp_directory)
    os.rmdir(temp_directory)

@api_view(['GET', 'POST'])
def picture_list(request):
    if request.method == 'GET':
        pictures = Picture.objects.all()
        serializer = PictureSerializer(pictures, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def group_pictures(request):
    if request.method == 'POST':
        if 'group_image' in request.FILES:
            image_file = request.FILES['group_image']
            filename = default_storage.save('one_images/' + image_file.name, image_file)
            path = 'one_images/' + image_file.name
            asyncio.run(compare(path))
            return Response({"message": f"Image saved successfully at {default_storage.url(filename)}"}, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def picture_detail(request, img):
    try:
        picture = Picture.objects.get(group_image="group_images/" + img)
    except Picture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PictureSerializer(picture)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PictureSerializer(picture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        picture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
