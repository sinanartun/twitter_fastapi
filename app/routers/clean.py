import nltk
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from ..models.clean import Clean

# Ensure the required NLTK data is downloaded
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Load the pre-trained model
model = joblib.load('logistic_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

def preprocess(text: str) -> str:
    # Convert to lower case
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove digits
    text = re.sub(r'\d', '', text)
    
    # Remove currency symbols
    text = re.sub(r'\$\w+', '', text)
    
    # Remove hyphens and strip whitespace
    text = text.replace('-', '').strip()
    
    # Remove stop words
    text = " ".join(word for word in text.split() if word not in stop_words)
    
    # Lemmatize words
    text = " ".join(lemmatizer.lemmatize(word) for word in text.split())
    
    return text

def predict_sentiment(text: str):
    cleaned_text = preprocess(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)
    return prediction[0]

def clean_text(clean: Clean):
    cleaned_text = preprocess(clean.text)
    sentiment = predict_sentiment(cleaned_text)
    return {"text": cleaned_text, "sentiment": sentiment}
