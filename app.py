from flask import Flask,request,jsonify
from funcs import getClasses,bagOfWords,load_JSON,ProcessData
from pathlib import Path
import numpy as np
from model import get_prediction
import os
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)

json_path = root / "input" / "intents.json"

classes = getClasses()
sorted_classes = sorted(classes)

json_data = load_JSON(json_path)
words,labels,training,output = ProcessData(json_data,train = False)

@app.route('/api',methods=['POST'])
def chat_output():
    data = request.get_json(force = True)

    #input text sent via POST request
    input_text = data["input"]
    
    #Prediction np array
    tag_pred = get_prediction([bagOfWords(input_text,words).tolist()])

    #Corresponding tag output
    chatOut_index = np.argmax(tag_pred)

    #Equivalent tag for the predicted index
    tag = sorted_classes[chatOut_index]

    #Getting the data for the corresponding tag in the JSON
    intents = json_data["intents"]

    reply = ""
    # confidence = chatOut[chatOut_index]

    #Loop to randomly choose a reply for the corresonding tag
    for i in range(len(intents)):
        if intents[i]["tag"] == tag:
            responses = intents[i]["responses"]
            reply = np.random.choice(responses, 1, replace=False)[0]  
            
    result={"reply":reply}

    response = jsonify(result)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(port=8000,debug=False)