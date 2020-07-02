print("Initializing Tensorflow environment.....")
import os
#Remove Tensorflow Messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
from tensorflow.python.util import deprecation
#Avoid Deprecation warnings
deprecation._PRINT_DEPRECATION_WARNINGS = False
import tensorflow as tf
from tensorflow import keras
from flask import Flask,request,jsonify
app = Flask(__name__) 
from funcs import getClasses,bagOfWords,load_JSON,ProcessData
from pathlib import Path
import numpy as np
# from model import get_prediction

print("Loaded Tensorflow and other libraries.....")

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Path(dir_path)

json_path = root / "input" / "intents.json"
saved_model_dir = "saved_model" 
model_name = "TChatBot"
model_version = "v1"

model_path = saved_model_dir + "/" + model_name + "/" + model_version

model = tf.keras.models.load_model(model_path)

@app.route('/api',methods=['POST'])
def chat_output():
    data = request.get_json(force = True)

    classes = getClasses()
    sort_classes = sorted(classes)

    json_data = load_JSON(json_path)
    words,labels,training,output = ProcessData(json_data,train = False)

    #input text sent via POST request
    input_text = data["input"]
    # model.summary()
    
    tag_pred = model.predict([bagOfWords(input_text,words)])

    chatOut_index = np.argmax(tag_pred)
    tag = sort_classes[chatOut_index]
    intents = json_data["intents"]
    reply = ""
    # confidence = chatOut[chatOut_index]

    #Loop to randomly choose a reply
    for i in range(len(intents)):
        if intents[i]["tag"] == tag:
            responses = intents[i]["responses"]
            reply = np.random.choice(responses, 1, replace=False)[0]  
            
    result={"reply":reply}

    return jsonify(result)

if __name__ == "__main__":
    app.run(port=8000,debug=False)