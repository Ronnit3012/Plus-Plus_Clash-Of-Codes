import requests
import os

API_URL = "https://api-inference.huggingface.co/models/nateraw/vit-age-classifier"
headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}

def age_predictor(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

img_file = "/content/amen.JPG"
resp = age_predictor(img_file)
age_pred = (resp[0])['label']
age_pred