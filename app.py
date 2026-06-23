import streamlit as st
import pickle
import numpy as np

# Load the saved model
mlr = pickle.load(open("mlr.pkl", "rb"))

st.title("Car MPG Prediction")

# Input fields (change these according to your dataset)
hp = st.number_input("Horse Power (HP)", min_value=0.0)
vol = st.number_input("Volume (VOL)", min_value=0.0)
sp = st.number_input("Speed (SP)", min_value=0.0)
wt = st.number_input("Weight (WT)", min_value=0.0)

# Predict button
if st.button("Predict MPG"):
    features = np.array([[hp, vol, sp, wt]])
    prediction = mlr.predict(features)

    st.success(f"Predicted MPG: {prediction[0]:.2f}")