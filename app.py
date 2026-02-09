import streamlit as st
from transformers import pipeline
import random

# 1. Page Configuration
st.set_page_config(page_title="VibeTune AI", page_icon="🎧", layout="centered")

# 2. Load Model (Cached so it only loads once)
@st.cache_resource
def load_classifier():
    # Uses a specialized DistilRoBERTa model for 7-way emotion classification
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

classifier = load_classifier()

# 3. Emotion-to-Music Mapping
MOOD_PLAYLISTS = {
    "joy": [
        "Walking on Sunshine - Katrina & The Waves",
        "Happy - Pharrell Williams",
        "Levitating - Dua Lipa",
        "Don't Stop Me Now - Queen"
    ],
    "sadness": [
        "Someone Like You - Adele",
        "Fix You - Coldplay",
        "The Night We Met - Lord Huron",
        "Yesterday - The Beatles"
    ],
    "anger": [
        "Killing In The Name - Rage Against The Machine",
        "In the End - Linkin Park",
        "Break Stuff - Limp Bizkit",
        "Thunderstruck - AC/DC"
    ],
    "fear": [
        "Bury a Friend - Billie Eilish",
        "Thriller - Michael Jackson",
        "Disturbia - Rihanna",
        "Somebody's Watching Me - Rockwell"
    ],
    "surprise": [
        "Bohemian Rhapsody - Queen",
        "Starman - David Bowie",
        "Electric Feel - MGMT",
        "Mr. Brightside - The Killers"
    ],
    "disgust": [
        "Bad Guy - Billie Eilish",
        "Uptown Funk - Bruno Mars",
        "You're So Vain - Carly Simon"
    ],
    "neutral": [
        "Weightless - Marconi Union",
        "Lofi Hip Hop - Chillhop Music",
        "Spiritual State - Nujabes",
        "Gymnopédie No. 1 - Erik Satie"
    ]
}

# 4. App UI
st.title("🎧 VibeTune AI")
st.write("Type a sentence about your day, and I'll match the emotion to a song.")
st.divider()

# User Input
user_input = st.text_area("How are you feeling?", placeholder="e.g., I'm so excited for the weekend!")

# Execution Logic
if st.button("Analyze Mood & Suggest Song"):
    if user_input.strip():
        with st.spinner("Analyzing your vibes..."):
            # Model Inference
            results = classifier(user_input)
            label = results[0]['label']
            score = results[0]['score']

            # Selection
            song_choice = random.choice(MOOD_PLAYLISTS.get(label, MOOD_PLAYLISTS["neutral"]))

            # Results Display
            st.subheader(f"Detected Emotion: **{label.title()}**")
            st.write(f"Confidence Level: {round(score * 100, 2)}%")
            st.progress(float(score))
            
            st.success(f"🎵 **Recommended Track:** {song_choice}")

            # Visual effects for specific moods
            if label == "joy":
                st.balloons()
            elif label == "anger":
                st.error("Let it all out. Here's a heavy track for you.")
            elif label == "sadness":
                st.info("It's okay to feel this way. Let the music help.")
    else:
        st.warning("Please enter some text so I can analyze it!")

# Footer
st.sidebar.markdown("### How it works")
st.sidebar.write("This app uses a **Transformer-based Deep Learning model** to detect 7 specific emotions in text. Unlike basic sentiment analysis, it understands context and nuance.")
