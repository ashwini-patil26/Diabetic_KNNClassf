from flask import Flask, jsonify, render_template, request

from project_app.utils import Diabetic

app = Flask(__name__)

@app.route("/") 
def hello_Patient():
    print("Welcome to Diabities HealthCare Centre")   
    return render_template("index.html")

@app.route("/predict_sickness", methods = ["POST", "GET"])
def get_prediction_diabetic():
    if request.method == "GET":
        print("We are in a GET Method")

        Glucose=eval(request.args.get("Glucose"))
        BloodPressure=eval(request.args.get("BloodPressure"))
        SkinThickness=eval(request.args.get("SkinThickness"))
        Insulin=eval(request.args.get("Insulin"))
        BMI=eval(request.args.get("BMI"))
        DiabetesPedigreeFunction=eval(request.args.get("DiabetesPedigreeFunction"))
        Age=eval(request.args.get("Age"))

        diab=Diabetic(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        pred_diab=diab.get_predicted_value()
        return render_template("index.html",prediction=pred_diab)
    
print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)