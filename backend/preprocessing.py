import cv2

def crop(image):
    # Set up haar cascade
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    # CV2 read the image to grayscale and process
    to_process = cv2.imread(image)
    #to_process = cv2.resize(to_process, (0, 0), fx=0.2, fy=0.2)
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
        print("num: " + str(len(faces)) + ", scale: " + str(scale_factor) + ", neighbours: " + str(min_neighbors))

    for (x, y, w, h) in faces:
        cropped_image = gray[y : y + h, x : x + w]
        #cv2.rectangle(to_process, (x,y), (x+w, y+h), (255,0,0), 2)
    return cropped_image

#img = "db/junhee.png"
img = "imgs/ianvandensteen.png"
'''face = crop(img)
cv2.imshow("img", face)
cv2.waitKey(0)'''
