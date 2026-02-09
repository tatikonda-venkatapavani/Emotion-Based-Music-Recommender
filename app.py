import streamlit as st
from textblob import TextBlob

# --- Page Configuration ---
st.set_page_config(
    page_title="VibeCheck | Emotion Recommender",
    page_icon="🎭",
    layout="centered"
)

# --- Data Store ---
def get_recommendation(mood):
    data = {
        "Happy": {
            "quote": "Happiness is not by chance, but by choice.",
            "song": "Can't Stop the Feeling! - Justin Timberlake",
            "color": "#FFD700"
        },
        "Sad": {
            "quote": "Even the darkest night will end and the sun will rise.",
            "song": "Fix You - Coldplay",
            "color": "#4682B4"
        },
        "Neutral": {
            "quote": "Life is a balance of holding on and letting go.",
            "song": "Weightless - Marconi Union",
            "color": "#808080"
        }
    }
    return data.get(mood)

# --- UI Layout ---
st.title("🎭 VibeCheck AI")
st.markdown("### Share your thoughts, and I'll match your energy.")

user_input = st.text_area("What's on your mind?", placeholder="I'm feeling really motivated today because...", height=150)

if st.button("Analyze Vibe"):
    if user_input.strip():
        # Sentiment Analysis
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity
        
        # Categorize Mood
        if polarity > 0.1:
            mood = "Happy"
        elif polarity < -0.1:
            mood = "Sad"
        else:
            mood = "Neutral"
        
        res = get_recommendation(mood)
        
        # Display Results
        st.divider()
        st.subheader(f"Detected Mood: {mood}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"✨ **Daily Quote**\n\n*{res['quote']}*")
        with col2:
            st.success(f"🎶 **Song Suggestion**\n\n{res['song']}")
            
        if mood == "Happy":
            st.balloons()
    else:
        st.warning("Please type something before analyzing!")

# --- Sidebar ---
st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ using Streamlit & TextBlob")
