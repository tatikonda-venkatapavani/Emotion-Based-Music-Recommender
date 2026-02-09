import streamlit as st
from textblob import TextBlob
import nltk

# --- Force Download of NLTK Data (Required for Deployment) ---
@st.cache_resource
def download_nltk_data():
    try:
        nltk.download('punkt_tab')
        nltk.download('brown')
    except Exception as e:
        st.error(f"Error downloading data: {e}")

download_nltk_data()

# --- Page Config ---
st.set_page_config(page_title="VibeCheck AI", page_icon="🎵")

# --- Recommendation Logic ---
recs = {
    "Happy": {
        "quote": "Most folks are as happy as they make up their minds to be. – Abraham Lincoln",
        "song": "Walking on Sunshine - Katrina & The Waves"
    },
    "Sad": {
        "quote": "The way I see it, if you want the rainbow, you gotta put up with the rain. – Dolly Parton",
        "song": "Fix You - Coldplay"
    },
    "Neutral": {
        "quote": "Peace comes from within. Do not seek it without. – Buddha",
        "song": "Weightless - Marconi Union"
    }
}

# --- UI Design ---
st.title("🎵 Emotion-Based Recommender")
st.write("Type a sentence below, and I'll suggest a song and a quote based on your mood.")

user_input = st.text_input("How are you feeling?", placeholder="It's been a long but productive day...")

if st.button("Analyze My Vibe"):
    if user_input.strip():
        # Sentiment Analysis
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity
        
        # Determine Category
        if polarity > 0.1:
            mood = "Happy"
            st.balloons()
        elif polarity < -0.1:
            mood = "Sad"
        else:
            mood = "Neutral"
        
        # Display Results
        st.divider()
        st.subheader(f"Detected Mood: {mood}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"✨ **Quote**\n\n{recs[mood]['quote']}")
        with col2:
            st.success(f"🎶 **Song**\n\n{recs[mood]['song']}")
    else:
        st.warning("Please enter some text first!")

st.markdown("---")
st.caption("Powered by Streamlit & TextBlob NLP")
