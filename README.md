# 📰 Fake News Detection Web App

A machine learning web application that detects whether a news article is **real** or **fake** using Natural Language Processing (NLP) and Logistic Regression.

---
## 📈 Dataset Source

This project uses a labeled dataset of real and fake news articles.

👉 [Fake and Real News Dataset – by Clément Bisaillon (Kaggle)](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
## 🚀 Live Demo

👉 [Click Here to Try the App](https://sseuygoshfjwkqy6y7zhgl.streamlit.app/)

---

## 📌 Features

- Detects fake news using user-input text
- ML model trained on labeled dataset (Real vs Fake)
- Text preprocessing using TF-IDF vectorizer
- Clean and interactive UI using Streamlit
- Deployed online and open-source on GitHub

---

## 💻 Tech Stack

- Python  
- Scikit-learn  
- Pandas & NumPy  
- NLTK  
- Streamlit  
- Git & GitHub

---

## 🧠 How it Works

1. Dataset of real and fake news articles is loaded
2. Preprocessing:
    - Lowercasing
    - Stopword removal
    - Punctuation removal
3. Features extracted using **TF-IDF Vectorizer**
4. Logistic Regression model trained to classify news
5. User inputs a news article → app predicts Real or Fake

---

## 📂 Project Structure
fake-news-detector-/
├── app.py              # Streamlit app
├── model.pkl           # Trained ML model
├── vectorizer.pkl      # TF-IDF vectorizer
├── requirements.txt    # Required libraries
├── README.md           # This file








