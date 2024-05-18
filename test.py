from deepface import DeepFace

mainpath = "imgs/img1.jpg"
for x in range(0,3):
    path2 = "stored-faces/" + str(x) + '.jpg'
    result = DeepFace.verify(img1_path = mainpath, img2_path = path2, enforce_detection=False)
    print(result)