from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def hello_world():
    return render_template("home.html")
@app.route('/login',methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/result',methods=['GET'])
def result():
    return render_template("result.html")

@app.route('/collection',methods=['GET'])
def collection():
    return render_template("collection.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    depth = int(request.form['depth'])
    sal = int(request.form['salinity'])
    lat=float(request.form['latitude'])
    lon = float(request.form['longitude'])
    # Make prediction
    
    prediction = model.predict([[depth,sal,lat,lon]])
   
    if prediction == 0:
        return '<script>alert("Fishing is not productive."); window.location="/";</script>'
    else:
        return '<script>alert("Fishing is productive."); window.location="/";</script>'
if __name__ == '__main__':
    app.run(debug=True)