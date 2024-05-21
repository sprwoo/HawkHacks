# YO! Send that to me!
> "You know how when you take a group photo and everyone asks you to send the picture to them?"

We developed an ML-based app to automatically send group photos to individuals within the photo via email.

We used **Django** Rest Framework to build endpoints that take in image and text data from the **React.js** frontend, processes the images, and stores corresponding text data into on an **Azure PostgreSQL server**.

We used **OpenCV** for image pre-processing and **DeepFace** to calculate for facial similarity.

The idea is that each user will upload a base image for their face.
Then, a group image is submitted, and we identify each face in the group image, comparing each unique face to the base image of each user.
For the faces in storage that match each unique face in the group photo, we automatically send an email with the group photo to the inputted emails of each user.

## If you want to run it for yourself...
- Clone the git repository
- Ensure you have Python and JavaScript installed, as well as pip and npm 
- Download all the requirements in requirements.txt (Some required packages are missing, so download as you go)
- Run ```python manage.py runserver```, followed by ```cd frontend``` and ```npm run dev```
- Open the local host link then register an image by clicking register and submitting name, email and a selfie (best image is face forwards with little background "noise")
- Submit a group photo
- Receive an email soon with the group photo

Submitted as a project for Wilfrid Laurier University's HawkHacks 2024.
