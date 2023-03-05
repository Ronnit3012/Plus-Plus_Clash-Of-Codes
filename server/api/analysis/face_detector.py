import cv2
import mediapipe as mp
import uuid
import os
import numpy as np
import urllib

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def face_detect(imageUrl):

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:

        req = urllib.request.urlopen(imageUrl)

        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)

        image = cv2.imdecode(arr, -1)
    
        # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Draw face detections of each face.
        if not results.detections:
            return "", 0.0

        annotated_image = image.copy()

        for detection in results.detections:
            mp_drawing.draw_detection(annotated_image, detection)

        face_prob = float(((str(results.detections[0]).split('\n'))[1]).split(':')[1])

        img_name = str(uuid.uuid4()) + '.png'

        img_path = os.path.abspath(__file__ + "/../../../static/annotated_img")

        cv2.imwrite(f'{img_path}/{img_name}', annotated_image)

        return img_name, str(face_prob)

print(face_detect('https://t4.ftcdn.net/jpg/00/76/27/53/360_F_76275384_mRNrmAI89UPWoWeUJfCL9CptRxg3cEoF.jpg'))