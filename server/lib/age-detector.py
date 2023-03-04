import requests
import os


API_URL = "https://api-inference.huggingface.co/models/nateraw/vit-age-classifier"
headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}

def age_predictor(imgURL):
    with open(imgURL, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    preds = response.json()
    return preds