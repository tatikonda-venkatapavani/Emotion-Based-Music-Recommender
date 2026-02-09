import streamlit as st
import random

# 1. App Configuration
st.set_page_config(page_title="Global MoodTune", page_icon="🎵")

st.markdown("""
    <style>
    .main { background-color: #121212; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #1DB954; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. Expanded Multi-Language Database
music_db = {
    "English": {
        "Happy": ["Walking on Sunshine - Katrina & The Waves", "Happy - Pharrell Williams"],
        "Sad": ["Someone Like You - Adele", "Fix You - Coldplay"],
        "Energetic": ["Power - Kanye West", "Eye of the Tiger - Survivor"],
        "Relaxed": ["Sunflower - Post Malone", "Weightless - Marconi Union"]
    },
    "Telugu": {
        "Happy": ["Butta Bomma (AVPL)", "Chilipiga (Orange)", "Super Machi (S/O Satyamurthy)"],
        "Sad": ["Oosupodu (Fidaa)", "Thalachi Thalachi (7G Brindavan Colony)"],
        "Energetic": ["Top Lesi Poddi (Iddarammayilatho)", "Ramulo Ramula (AVPL)"],
        "Relaxed": ["Samayama (Hi Nanna)", "Gundelonaa (Ori Devuda)"]
    },
    "Hindi": {
        "Happy": ["Balam Pichkari (YJHD)", "London Thumakda (Queen)"],
        "Sad": ["Agar Tum Saath Ho (Tamasha)", "Channa Mereya (ADHM)"],
        "Energetic": ["Mauja Hi Mauja (Jab We Met)", "Kar Gayi Chull"],
        "Relaxed": ["Tum Se Hi (Jab We Met)", "Iktara (Wake Up Sid)"]
    },
    "Tamil": {
        "Happy": ["Arabic Kuthu (Beast)", "Aaluma Doluma (Vedalam)"],
        "Sad": ["Poo Nee Poo (3)", "Kanave Kanave (David)"],
        "Energetic": ["Vaathi Coming (Master)", "Rakita Rakita (Jagame Thandhiram)"],
        "Relaxed": ["Munbe Vaa (Sillunu Oru Kaadhal)", "Vaseegara (Minnale)"]
    }
}

# 3. App UI
st.title("🎵 Global MoodTune")
st.subheader("Select your language and mood for a recommendation.")

# Language Selection
selected_lang = st.selectbox("Choose your Preferred Language:", list(music_db.keys()))

st.write(f"How is your mood in {selected_lang}?")

# 4. Logic & Display
moods = ["Happy", "Sad", "Energetic", "Relaxed"]
cols = st.columns(4)
selected_mood = None

for i, mood in enumerate(moods):
    if cols[i].button(mood):
        selected_mood = mood

if selected_mood:
    st.divider()
    # Pulling from the nested dictionary based on Lang -> Mood
    songs = music_db[selected_lang][selected_mood]
    recommendation = random.choice(songs)
    
    st.markdown(f"### Current Mood: **{selected_mood}**")
    st.success(f"**Recommended {selected_lang} Track:** \n\n {recommendation}")
    st.info(f"Go play this on Spotify or YouTube!")
else:
    st.info("Pick a mood to see the magic.")
