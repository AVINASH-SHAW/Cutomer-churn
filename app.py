## importing requred libraries
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler

# load the logistic regression model file
filename = "logistic_regression_model.pkl"
classifier = pickle.load(open(filename,'rb')) 

# loading the Minmax scaler
scalerfile  = 'scaler.sav'
scaler = pickle.load(open(scalerfile, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        tenure = int(request.form["tenure"])
        MonthlyCharges = int(request.form["MonthlyCharges"])
        InternetService_Fiber optic = int(request.form["InternetService_Fiber optic"])
        gender_Male = int(request.form["gender_Male"])
        PaperlessBilling = int(request.form["PaperlessBilling"])
        Contract_Two year = int(request.form["Contract_Two year"])
        
        data = np.array[['tenure', 'MonthlyCharges', 'InternetService_Fiber optic','gender_Male', 'PaperlessBilling', 'Contract_Two year']]
        data_scaled = scaler.transform(data)
        
        my_prediction = classifier.predict(data_scaled)
        
        if my_prediction==0:
            return render_template("index.html", prediction_text="Hurray!! The Customer will retain")
        else:
            return render_template("index.html", prediction_text  = "Sorry!! The Customer will churn")
    
    else:
        render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug = True)
    
      