from flask import Flask,request,url_for,render_template,redirect
import os
app = Flask(__name__,template_folder="Template") 
import model 
@app.route('/',methods=['POST'])
def index():
    #there is a index.html which will provide the data to the flask
    #Reads data from the html textfield
    #Data is taken from the textfield
    text = request.form['text']
    #Reply from chatbot
    reply = model.get_reply(text)
    #parsing the reply in a dictionary to be used in result
    result={"reply":reply}
    return render_template('result.html', result = result)
    #Result.html is supposed to show the reply