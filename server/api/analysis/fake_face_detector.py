import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import urllib

model_path = os.path.abspath(__file__ + "/../../../model/MesoFace.h5")

loaded_model = tf.keras.models.load_model(model_path)

def fake_face_detector(imgURL):

    req = urllib.request.urlopen(imgURL)

    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)

    img = cv2.imdecode(arr, -1)

    # img = cv2.imread(imgURL)
    img = cv2.resize(img, (256, 256))
    img = np.reshape(img,(1, 256, 256, 3))
    outputs = loaded_model(img)
    class_names = ['fake_image', 'real_image']

    # Get index of class with highest probability
    predicted_class_index = np.argmax(outputs)

    # Map index to class name
    predicted_class_name = class_names[predicted_class_index]

    preds = list(np.array(outputs[0]))

    preds = [str(p) for p in preds]

    return preds, predicted_class_name
