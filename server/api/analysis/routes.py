from flask import Blueprint, request, jsonify
import json

from .age_detector import age_predictor
from .face_detector import face_detect
from .gender_detector import detectGender
from .fake_face_detector import fake_face_detector


analysis_bp = Blueprint(
    'analysis_bp', __name__,
)


@analysis_bp.route('', methods=["POST"])
def analysis():
    try:

        imgURL = request.json["imgURL"]

        res_body = {
            'orignalImg': imgURL,
            'annotatedImg': "Invalid",
            'isReal': "Invalid",
            'isRealPreds': {
                'real': "Invalid",
                'fake': "Invalid"
            },
            'genderPreds': {
                'male': "Invalid",
                'female': "Invalid"
            },
            'gender': "Invalid",
            'age': "Invalid",
            'agePreds': "Invalid",
            'faceProb': "Invalid",
            'message': 'failed'
        }

        # img probability

        annotated_img_path, probability_of_face = face_detect(imgURL)

        res_body['faceProb'] = probability_of_face

        if probability_of_face == 0:
            res_body['message'] = 'probability_of_face == 0'
            return json.dumps(res_body)

        res_body['annotatedImg'] = annotated_img_path

        # fake_image
        imgAuthPreds, imgAuth = fake_face_detector(imgURL)

        res_body['isReal'] = imgAuth
        res_body['isRealPreds']['fake'] = imgAuthPreds[0]
        res_body['isRealPreds']['real'] = imgAuthPreds[1]

        if imgAuth == 'fake_image':
            res_body['message'] = "imgAuth == 'fake_image'"
            return json.dumps(res_body)

        # gender
        genderPreds, gender = detectGender(imgURL)

        res_body['genderPreds'] = genderPreds
        res_body['gender'] = gender

        # age

        age = age_predictor(imgURL)

        res_body['age'] = age

        res_body['message'] = "sucess"

        return json.dumps(res_body)

    except Exception as Argument:
        print(Argument)
        return json.dumps(res_body)
