import requests
import os
from dotenv import load_dotenv
load_dotenv()


API_URL = "https://api-inference.huggingface.co/models/nateraw/vit-age-classifier"
headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}

def age_predictor(imgURL):
    response = requests.post(API_URL, headers=headers, data=imgURL)
    preds = response.json()
    return preds[0]['label']
