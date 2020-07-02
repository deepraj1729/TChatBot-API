import numpy as np
import json
import requests

MODEL_URL='http://localhost:8501/v1/models/pets:predict'

def get_prediction(bag_of_words):

    data = json.dumps({
        'output': bag_of_words.tolist()
    })

    response = requests.post(MODEL_URL, data=data.encode('utf-8'))
    result = json.loads(response.text)
    return result

