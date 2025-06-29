import streamlit as st
import joblib

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("📰 Fake News Detector")
text = st.text_area("Enter news article:")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter some news text")
    else:
        vec = vectorizer.transform([text])
        result = model.predict(vec)[0]
        if result == 1:
            st.error("🔴 Fake News Detected!")
        else:
            st.success("🟢 This is Real News!")