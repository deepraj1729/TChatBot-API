from flask import jsonify
import numpy as np
import json
import requests

MODEL_URL='https://tchatbot1.herokuapp.com/v1/models/chat_model:predict'

def get_prediction(bag_of_words):

    data = json.dumps({
    "signature_name": "serving_default",
    "instances": bag_of_words
    })
    headers = {"content-type": "application/json"}

    response = requests.post(url=MODEL_URL, data=data, headers=headers)
    result = json.loads(response.text)
    prediction = np.squeeze(result['predictions'][0])
    return prediction

