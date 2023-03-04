import cv2
import mediapipe as mp
import uuid
import os


mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def borderBox(imageUrl):

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        image = cv2.imread(imageUrl)

        # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Draw face detections of each face.
        if not results.detections:
            pass

        annotated_image = image.copy()

        for detection in results.detections:
            mp_drawing.draw_detection(annotated_image, detection)

        img_name = uuid.uuid4() + '.png'

        img_path = os.path.abspath(__file__ + "/../../../static/img")

        cv2.imwrite(f'{img_path}/{img_name}', annotated_image)

        return img_name
