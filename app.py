import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

# Title
st.title("Heart Disease Risk Predictor")

# Inputs
age = st.slider("Age", 20, 100)
chol = st.slider("Cholesterol", 100, 400)
thalach = st.slider("Max Heart Rate", 60, 220)

# Convert input
input_data = np.array([[age, chol, thalach]])

# Predict
if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk")