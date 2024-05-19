import cv2

# ngl I don't know what type these should be :3
# image comes directly from frontend/Django and returns an processed image.
def crop(image):
    '''crop(image) finds a face within a picture, crops it to fit the face and grayscales the picture.
    Ideally, the user will send a front-facing picture with little to no background "noise." We preprocess this image
    to store it into our database so we would not have to process it everytime we want to pull images from the database.'''

    # Set up haar cascade
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    # OpenCV read the image to grayscale and process
    to_process = cv2.imread(image)
    #to_process = cv2.resize(to_process, (0, 0), fx=0.2, fy=0.2) # Testing purposes
    gray = cv2.cvtColor(to_process, cv2.COLOR_BGR2GRAY) 

    # Crop for the face
    scale_factor = 1.3
    min_neighbors = 5
    last_changed = False # False for min_neighbors, True for scale_factor
    times = 1

    while(True):
        faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors = min_neighbors)

        # An incredibly basic algorithm to narrow down the faces it detects
        # It will loop until it detects ONE face and returns that face, so
        # it doesn't actually find a face but rather narrows down options
        # This, realistically, was only made to make sure we either find a face or
        # find only ONE face. 
        if (len(faces) > 1):
            if (last_changed):
                min_neighbors += 1
                last_changed = not last_changed
            elif (not last_changed):
                scale_factor += 0.1 / times
                last_changed = not last_changed
                times += 1
        elif (len(faces) < 1):
            if (last_changed):
                min_neighbors -= 1
                last_changed = not last_changed
            elif (not last_changed):
                scale_factor -= 0.1 / times
                last_changed = not last_changed
                times += 1
        else: break
        
        # Testing purposes
        print("num: " + str(len(faces)) + ", scale: " + str(scale_factor) + ", neighbours: " + str(min_neighbors))

    # Store the grayscaled + cropped image
    for (x, y, w, h) in faces:
        cropped_image = gray[y : y + h, x : x + w]
        #cv2.rectangle(to_process, (x,y), (x+w, y+h), (255,0,0), 2)
    return cropped_image

# Testing purposes
#img = "db/junhee.png"
img = "imgs/ianvandensteen.png"
'''face = crop(img)
cv2.imshow("img", face)
cv2.waitKey(0)'''
