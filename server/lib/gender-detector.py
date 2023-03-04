import cv2

genderProto = "../config/gender_deploy.prototxt"
genderModel = "../model/gender_net.caffemodel"
genderNet = cv2.dnn.readNet(genderModel, genderProto)
genderList = ['Male', 'Female']

# img_path = "/content/amen.JPG"

def detectGender(imgURL):
    face = cv2.imread(imgURL)
    blob = cv2.dnn.blobFromImage(face, 1, (227, 227), swapRB=False)
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    gender = genderList[genderPreds[0].argmax()]
    return genderPreds, gender

print(detectGender('../../devang_pfp.jpg'))