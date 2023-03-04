import cv2

import os
absolute_path = os.path.abspath(__file__)
proto_path = os.path.abspath(__file__ + "/../../../config/gender_deploy.prototxt")
model_path = os.path.abspath(__file__ + "/../../../model/gender_net.caffemodel")



genderProto = os.path.abspath(__file__ + "/../../../config/gender_deploy.prototxt")
genderModel = os.path.abspath(__file__ + "/../../../model/gender_net.caffemodel")
genderNet = cv2.dnn.readNet(genderModel, genderProto)
genderList = ['Male', 'Female']


def detectGender(imgURL):
    face = cv2.imread(imgURL)
    blob = cv2.dnn.blobFromImage(face, 1, (227, 227), swapRB=False)
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    gender = genderList[genderPreds[0].argmax()]
    return genderPreds, gender
