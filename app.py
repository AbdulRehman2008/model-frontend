# Step 3: Streamlit frontend

import streamlit as st
import requests

st.title("🎬 IMDB Movie Review Sentiment")
st.write("Type a movie review and the model will predict if it is Positive or Negative.")

# Text input
review = st.text_area("Enter your movie review here:")

# Button
if st.button("Predict"):
    if review == "":
        st.warning("Please write a review first.")
    else:
        # Send request to FastAPI
        response = requests.post("http://localhost:8000/predict", json={"text": review})
        result = response.json()

        sentiment = result["sentiment"]
        score = result["score"]

        if sentiment == "Positive":
            st.success("Sentiment: Positive")
        else:
            st.error("Sentiment: Negative")

        st.write("Model Score:", score)
