import streamlit as st
import random

# 1. App Configuration & Styling
st.set_page_config(page_title="MoodTune", page_icon="🎵")

st.markdown("""
    <style>
    .main {
        background-color: #121212;
        color: white;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #1DB954;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Local Music Database (No API needed)
mood_data = {
    "Happy": {
        "songs": ["Walking on Sunshine - Katrina & The Waves", "Happy - Pharrell Williams", "Don't Stop Me Now - Queen"],
        "emoji": "😊",
        "color": "#FFD700"
    },
    "Sad": {
        "songs": ["Someone Like You - Adele", "Fix You - Coldplay", "Yesterday - The Beatles"],
        "emoji": "😢",
        "color": "#1E90FF"
    },
    "Energetic": {
        "songs": ["Power - Kanye West", "Eye of the Tiger - Survivor", "Can't Stop - RHCP"],
        "emoji": "⚡",
        "color": "#FF4500"
    },
    "Relaxed": {
        "songs": ["Weightless - Marconi Union", "Sunflower - Post Malone", "Morning - Edvard Grieg"],
        "emoji": "🧘",
        "color": "#98FB98"
    }
}

# 3. App UI
st.title("🎵 MoodTune")
st.subheader("Your manual emotion-based music curator.")

st.write("How are you feeling right now?")

# Create a layout with columns for buttons
cols = st.columns(len(mood_data))

selected_mood = None

for i, (mood, details) in enumerate(mood_data.items()):
    if cols[i].button(f"{details['emoji']}\n{mood}"):
        selected_mood = mood

# 4. Recommendation Logic
if selected_mood:
    st.divider()
    song = random.choice(mood_data[selected_mood]["songs"])
    
    st.markdown(f"### You're feeling <span style='color:{mood_data[selected_mood]['color']}'>{selected_mood}</span>", unsafe_allow_html=True)
    st.success(f"**Recommended Track:** {song}")
    
    # Adding a fun tip
    st.info("💡 Tip: Search for this song on your favorite music player!")
else:
    st.info("Click a mood above to get a recommendation.")
