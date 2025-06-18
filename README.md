# 📰 Fake News Detection using Machine Learning & Deep Learning

This project aims to accurately classify news articles as real or fake using both traditional machine learning algorithms and deep learning models. It involves web scraping, text preprocessing, feature extraction, model training, evaluation, and result visualization.

---

## 🚀 Workflow Overview

1. **Data Collection**  
   - Scraped real and fake news articles from [AP News](https://apnews.com/) using Selenium.

2. **Data Preprocessing**  
   - Performed lowercasing, punctuation removal, and tokenization to clean the text data.

3. **Feature Extraction**  
   - Used **Bag-of-Words (BoW)** and **TF-IDF** for text vectorization.

4. **Modeling**
   - **Machine Learning**:
     - Logistic Regression (with BoW & TF-IDF)
     - Naive Bayes (with BoW & TF-IDF)
   - **Deep Learning**:
     - CNN (10 epochs)
     - RNN (10 epochs)

5. **Evaluation**  
   - Accuracy, Precision, Recall, and F1-score metrics.

6. **Visualization**  
   - Used Plotly for interactive graphs:
     - Confusion Matrix
     - ROC Curve
     - Model Accuracy Comparison

---

## 🛠️ Tech Stack

- Python
- Selenium
- Scikit-learn
- TensorFlow / Keras
- Plotly
- Pandas, NumPy

---

## 📊 Results Summary

- CNN performed best among deep learning models.
- Logistic Regression with TF-IDF outperformed Naive Bayes in ML models.
- Visualizations helped clearly compare model performance.

---

## 📁 Folder Structure

