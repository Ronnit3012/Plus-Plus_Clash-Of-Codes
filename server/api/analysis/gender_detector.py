import cv2
import numpy as np
import os
import urllib

absolute_path = os.path.abspath(__file__)
proto_path = os.path.abspath(__file__ + "/../../../config/gender_deploy.prototxt")
model_path = os.path.abspath(__file__ + "/../../../model/gender_net.caffemodel")



genderProto = os.path.abspath(__file__ + "/../../../config/gender_deploy.prototxt")
genderModel = os.path.abspath(__file__ + "/../../../model/gender_net.caffemodel")
genderNet = cv2.dnn.readNet(genderModel, genderProto)
genderList = ['Male', 'Female']


def detectGender(imgURL):

    req = urllib.request.urlopen(imgURL)

    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)

    img = cv2.imdecode(arr, -1)

    blob = cv2.dnn.blobFromImage(img, 1, (227, 227), swapRB=False)
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    gender = genderList[genderPreds[0].argmax()]
    genderPreds = [str(g) for g in genderPreds]
    return genderPreds, gender
