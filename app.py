import streamlit as st
import sklearn
import pickle
import numpy as np
with open("diabetes_RF_MODEL.pkl", "rb") as model_file:
    model = pickle.load(model_file)
st.title("Diabetes Predictor ")
st.write("Enter the Person Data")
gender_options = ["Male", "Female"]
selected_gender_str = st.radio("Select your gender:", gender_options)

if selected_gender_str == "Male":
    gender_input_for_model = 0
else:
    gender_input_for_model = 1

st.write(f"You selected: {selected_gender_str} (Model input: {gender_input_for_model})")

age = st.slider("Age", min_value=0.0, max_value=100.0, step=1.0)
hypertension = st.slider("hypertension", min_value=0.0, max_value=1.0, step=1.0)
heart_disease = st.slider("Heart_disease", min_value=0.0, max_value=1.0, step=1.0)
bmi  = st.slider("BMI", min_value=1.0, max_value=50.0, step=1.0)
HbA1c_level  = st.slider("HbA1c_level", min_value=2.0, max_value=10.0, step=0.2)
blood_glucose_level  = st.slider("Blood_glucose_level", min_value=50.0, max_value=300.0, step=1.0)
if st.button("Predict"):
    features = np.array([[gender_input_for_model,age,hypertension,heart_disease,bmi,HbA1c_level,blood_glucose_level]])
    prediction = model.predict(features)
    if (prediction[0] ==1):
        st.write(f"The person has high chances of  Diabetes ")
    else: 
         st.write(f"The person has less chances of  Diabetes ")

         

