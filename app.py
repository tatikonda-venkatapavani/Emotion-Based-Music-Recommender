import streamlit as st
from textblob import TextBlob
import nltk

# --- NLTK Data Setup (Crucial for Streamlit Cloud) ---
@st.cache_resource
def load_nltk():
    nltk.download('punkt_tab')
    nltk.download('brown')

load_nltk()

# --- App Data ---
recommendations = {
    "Happy": {"quote": "Happiness is a direction, not a place.", "song": "Happy - Pharrell Williams"},
    "Sad": {"quote": "Even the darkest night will end and the sun will rise.", "song": "Someone Like You - Adele"},
    "Neutral": {"quote": "Life is a balance of holding on and letting go.", "song": "Weightless - Marconi Union"}
}

# --- Streamlit UI ---
st.title("🎵 Emotion-Based Recommender")
user_input = st.text_input("How are you feeling?", placeholder="Type here...")

if st.button("Get Recommendation"):
    if user_input:
        # NLP Processing
        blob = TextBlob(user_input)
        score = blob.sentiment.polarity
        
        # Determine Mood
        if score > 0.1: mood = "Happy"
        elif score < -0.1: mood = "Sad"
        else: mood = "Neutral"
        
        # Show Results
        st.divider()
        st.subheader(f"Mood Detected: {mood}")
        st.info(f"✨ Quote: {recommendations[mood]['quote']}")
        st.success(f"🎶 Song: {recommendations[mood]['song']}")
    else:
        st.warning("Please enter some text!")
