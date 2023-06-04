import numpy as np
import pandas as pd
import pickle
import json
import warnings
warnings.filterwarnings("ignore")
import config
class Diabetic():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age
    
    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
        #with open("KNN_model.pkl","rb") as f:

            self.knn_clf=pickle.load(f)

        with open(config.STD_FILE_PATH,"rb") as f:
        #with open("Scaling.pkl","rb") as f:
            self.std_scalar=pickle.load(f)

        
        with open(config.JSON_FILE_PATH,"r") as f:
        #with open("project_data.json","r") as f:
            self.json_data=json.load(f)     

    def get_predicted_value(self):
        
        self.load_models()  
    
        
        test_array = np.array([[self.Glucose,self.BloodPressure,self.SkinThickness,self.Insulin,self.BMI,self.DiabetesPedigreeFunction,self.Age]])

        self.scaled_array = self.std_scalar.transform(test_array)
        prediction=self.knn_clf.predict(self.scaled_array)[0]

        if prediction==0:
            return "Person is having Diabetics"
        else:
            return "No,Person is not having Diabetics"

        

if __name__== "__main__":
    Glucose=148.000
    BloodPressure=50.000
    SkinThickness=35.000
    Insulin=0.000
    BMI=33.600
    DiabetesPedigreeFunction=0.627
    Age=50.000
    

    diab=Diabetic(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    pred_diab=diab.get_predicted_value()
    print("Prediction of diabetic:",pred_diab) 