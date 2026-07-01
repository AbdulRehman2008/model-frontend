import streamlit as st
import requests

st.title("MNIST Digit Classifier")

BACKEND_URL = "model-backend-production-ec92.up.railway.app"

uploaded_file = st.file_uploader("Upload a digit image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, width=150)

    if st.button("Predict"):
        response = requests.post(f"{BACKEND_URL}/predict", files={"file": uploaded_file})
        result = response.json()
        st.write("Predicted Digit:", result["predicted_digit"])
