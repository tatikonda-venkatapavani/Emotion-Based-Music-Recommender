import streamlit as st
from transformers import pipeline
import random

# 1. Load the Emotion Detection Model (Cached to prevent reloading on every click)
@st.cache_resource
def load_classifier():
    # This specific model is trained to detect 7 distinct emotions
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

classifier = load_classifier()

# 2. Mood-to-Music Library
MOOD_PLAYLISTS = {
    "joy": ["'Happy' - Pharrell Williams", "'Walking on Sunshine' - Katrina & The Waves", "'Levitating' - Dua Lipa"],
    "sadness": ["'Someone Like You' - Adele", "'Fix You' - Coldplay", "'The Night We Met' - Lord Huron"],
    "anger": ["'Break Stuff' - Limp Bizkit", "'In the End' - Linkin Park", "'Killing in the Name' - RATM"],
    "fear": ["'Thriller' - Michael Jackson", "'Bury a Friend' - Billie Eilish", "'Disturbia' - Rihanna"],
    "surprise": ["'Bohemian Rhapsody' - Queen", "'Starman' - David Bowie", "'Electric Feel' - MGMT"],
    "disgust": ["'Uptown Funk' - Bruno Mars", "'Bad Guy' - Billie Eilish"],
    "neutral": ["'Weightless' - Marconi Union", "'Lofi Beats' - Chillhop Radio"]
}

# 3. Streamlit Interface
st.set_page_config(page_title="VibeTune AI", page_icon="🎧")

st.title("🎧 VibeTune AI")
st.markdown("---")

user_input = st.text_area("Tell me how you're feeling today:", placeholder="I've had a long day and just want to relax...")

if st.button("Get Recommendation"):
    if user_input.strip():
        with st.spinner("Analyzing the vibes..."):
            # Model prediction
            results = classifier(user_input)
            label = results[0]['label']
            score = results[0]['score']

            # Map results to our playlist
            # The model returns labels like 'joy', 'sadness', etc.
            song_choice = random.choice(MOOD_PLAYLISTS.get(label, MOOD_PLAYLISTS["neutral"]))

            # Display Result
            st.write(f"### Detected Emotion: **{label.upper()}**")
            st.progress(score) # Shows how confident the AI is
            
            st.success(f"🎶 Based on your mood, you should listen to: **{song_choice}**")
            
            # Simple UI flourish based on emotion
            if label == "joy":
                st.balloons()
    else:
        st.warning("Please type something so I can feel your vibe!")

---
### Why this is better:
* **Context Awareness:** If you type "I'm killing it at work!", `TextBlob` might get confused by the word "killing." This model knows that's a **Joy** sentiment.
* **Granularity:** Instead of just "Positive/Negative," you now have 7 distinct emotional categories.
* **Confidence Scores:** The code includes a progress bar showing the model's confidence (`score`) in its prediction.

**Would you like me to help you integrate the Spotify API so these songs show up as playable embedded widgets?**
