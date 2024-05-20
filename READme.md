We developed an ML-based app to automatically send group photos to individuals within the photo via email.

We used Django Rest Framework to build endpoints that take in image and text data from the **React.js** frontend, processes the images, and stores corresponding text data into on an **Azure PostgreSQL server**.

We used **OpenCV** for image pre-processing and **DeepFace** to calculate for facial similarity, thereby sending.

The idea is that each user will upload a base image for their face.
Then, a group image is submitted, and we identify each face in the group image, comparing each unique face to the base image of each user.
For the faces in storage that match each unique face in the group photo, we automatically send an email with the group photo to the inputted emails of each user.

Submitted as a project at HawkHacks 2024.

