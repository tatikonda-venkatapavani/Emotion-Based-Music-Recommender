import streamlit as st
import random

st.set_page_config(page_title="VibeCheck Music", page_icon="🎵")

# --- DATABASE LOGIC ---
# Strictly categorized by actual musical vibe
music_db = {
    "Telugu": {
        "Happy": ["Butta Bomma (AVPL)", "Chilipiga (Orange)", "Super Machi (S/O Satyamurthy)", "Ramulo Ramula", "Inkem Inkem Kaavaale", "Cinema Choopistha Mava", "Blockbuster", "He's So Cute", "Dhimmathirigae", "Aagadu Title"],
        "Sad": ["Oosupodu (Fidaa)", "Thalachi Thalachi (7G)", "Evare (Premam)", "Urike Chilaka", "Adiga Adiga (Ninnu Kori)", "Priyathama (Majili)", "Manasa (Munna)", "Life of Ram", "Yemainado", "Kanulanu Chade"],
        "Energetic": ["Top Lesi Poddi", "Dhamki Title", "Kurchi Madathapetti", "Bullet Song", "Naatu Naatu", "Jai Balayya", "Srivalli", "Mind Block", "Jigelu Rani", "Saami Saami"],
        "Romantic": ["Samajavaragamana", "Maate Vinadhuga", "Ay Pilla", "Emito Idhi", "Kannullona", "Neevalle", "Hridayam Lopala", "Nadhive", "Mellaga Karagani", "Undiporaadhey"],
        "Angry": ["Dabidi Dibidi", "Ragile Ragile", "Thee Thalapathy (Telugu)", "Shadow Title", "Don Seenu", "Mirchi Title", "Baahubali (Shivuni Aana)", "Bhairava Anthem", "Singham Title", "Bheemla Nayak Title"]
    },
    "Hindi": {
        "Happy": ["Balam Pichkari", "London Thumakda", "Mauja Hi Mauja", "Galla Goodiyan", "Zingaat", "Badtameez Dil", "Aankh Marey", "Kala Chashma", "Abhi Toh Party", "Kar Gayi Chull"],
        "Sad": ["Agar Tum Saath Ho", "Channa Mereya", "Tum Hi Ho", "Kabira", "Tujhe Kitna Chahne Lage", "Bekhayali", "Humari Adhuri Kahani", "Duaa", "Abhi Mujh Mein Kahin", "Phir Le Aya Dil"],
        "Energetic": ["Malhari", "Zinda (BMB)", "Sultan Title", "Dhating Naach", "Sheila Ki Jawani", "Dilbar", "Bom Diggy Diggy", "Garmi", "Jai Jai Shivshankar", "Muqabla"],
        "Romantic": ["Raataan Lambiyan", "Pee Loon", "Tum Kya Mile", "Pal Ek Pal", "Hawayein", "Ban Ja Rani", "Qaafirana", "Nazm Nazm", "Dil Diyan Gallan", "Kesariya"],
        "Angry": ["Aarambh Hai Prachand", "Sadda Haq", "Apna Time Aayega", "Bhaag D.K. Bose", "Gully Boy Rap", "Khalibali", "Agneepath Theme", "Mera Wala Dance", "Zinda", "Sultan Title"]
    },
    "English": {
        "Happy": ["Happy - Pharrell", "Uptown Funk", "Shake It Off", "Can't Stop The Feeling", "Levitating", "Dynamite", "Stay", "I'm Yours", "Sugar", "Shut Up and Dance"],
        "Sad": ["Someone Like You", "Fix You", "Stay With Me", "The Night We Met", "Hurt", "Driver's License", "Let Her Go", "Lovely", "Falling", "Yesterday"],
        "Energetic": ["Power - Kanye", "Eye of the Tiger", "Thunderstruck", "Believer", "Can't Hold Us", "Lose Yourself", "Blinding Lights", "Stronger", "Till I Collapse", "Centuries"],
        "Romantic": ["Perfect", "All of Me", "Thinking Out Loud", "Just The Way You Are", "A Thousand Years", "Say You Won't Let Go", "Lover", "My Heart Will Go On", "Beautiful In White", "Shallow"],
        "Angry": ["In The End", "Killing In The Name", "Smells Like Teen Spirit", "Break Stuff", "Walk (Pantera)", "Down With The Sickness", "One Step Closer", "Bulls On Parade", "Remember The Name", "Numb"]
    }
}

# --- UI INTERFACE ---
st.title("🎧 Precise Mood Recommender")
st.write("Ensuring the music actually matches your current state.")

# Selectors
col_a, col_b = st.columns(2)
with col_a:
    lang = st.selectbox("Language", list(music_db.keys()))
with col_b:
    mood = st.selectbox("Current Mood", list(music_db[lang].keys()))

if st.button(f"Generate {mood} Playlist"):
    st.divider()
    
    # Logic: Get the specific list for Lang + Mood
    playlist = music_db[lang][mood]
    
    # Shuffle so it's not the same order every time
    random.shuffle(playlist)
    
    st.subheader(f"Showing top {len(playlist)} tracks for {mood} ({lang})")
    
    # Visualization of the Logic
    
    
    for i, song in enumerate(playlist, 1):
        # Create a search query link
        search_query = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
        st.markdown(f"**{i}. {song}** &nbsp; [Listen on YouTube]({search_query})")
    
    st.success("Playlist synchronized to your mood!")
