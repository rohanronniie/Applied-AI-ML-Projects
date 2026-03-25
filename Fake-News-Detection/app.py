import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Fake News Detection")

st.write("Enter news text to check if it is real or fake")

text_input = st.text_area("Enter News Article")

if st.button("Predict"):
    if text_input.strip() == "":
        st.warning("Please enter some text")
    else:
        vectorized_text = vectorizer.transform([text_input])
        prediction = model.predict(vectorized_text)

        if prediction[0] == 0:
            st.error("Fake News ❌")
        else:
            st.success("Real News ✅")