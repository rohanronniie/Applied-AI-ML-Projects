import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("fraud_model.pkl")

st.title("Credit Card Fraud Detection")

st.write("Enter transaction details")

# Since dataset has many features, we simulate input
amount = st.number_input("Transaction Amount", value=100.0)

# Create input array (30 features like dataset)
input_data = np.array([[amount]*30])

if st.button("Check Fraud"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Fraudulent Transaction Detected")
    else:
        st.success("Transaction is Safe")