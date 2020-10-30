from flask import Flask, render_template, request
import json
from tools import model
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction",methods=['POST'])
def prediction():
    return render_template("prediction.html")

@app.route("/reponse",methods=['POST'])
def reponse():
    
    input_age       = request.form.get('input_age')
    input_marital   = request.form.get('input_marital')
    input_education = request.form.get('input_education')
    input_job       = request.form.get('input_job')
    input_default   = request.form.get('input_default')
    input_balance   = request.form.get('input_balance')
    input_housing   = request.form.get('input_housing')
    input_loan      = request.form.get('input_loan')
    input_campaign  = request.form.get('input_campaign')
    input_duration  = request.form.get('input_duration')
    input_pdays     = request.form.get('input_pdays')
    input_previous  = request.form.get('input_previous')
    input_poutcome  = request.form.get('input_poutcome')

    parametres = [input_age,input_job,input_marital,input_education,input_default,input_balance,input_housing,input_loan,input_duration,input_campaign,input_pdays,input_previous,input_poutcome]
    prediction=model(parametres)
    #print(prediction)
    return render_template("reponse.html",prediction=prediction)
    #return render_template("reponse.html")

if __name__ == "__main__":
    app.run()

