import streamlit as st
import requests

st.title("🎬 IMDB Movie Review Sentiment")
st.write("Type a movie review and the model will predict if it is Positive or Negative.")

review = st.text_area("Enter your movie review here:")

if st.button("Predict"):
    if review == "":
        st.warning("Please write a review first.")
    else:
        response = requests.post("https://movie-model-backend-production.up.railway.app/predict", json={"text": review})
        result = response.json()
        sentiment = result["sentiment"]
        score = result["score"]

        if sentiment == "Positive":
            st.success("Sentiment: Positive 😊")
        else:
            st.error("Sentiment: Negative 😞")

        st.write("Model Score:", score)
