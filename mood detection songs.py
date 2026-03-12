
import streamlit as st
import random
import urllib.parse

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Mood Playlist Generator",
    page_icon="🎧",
    layout="centered"
)

# ---------------- CUSTOM CSS (PROFESSIONAL DESIGN) ---------------- #

st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color: white;
}

.main-card {
background: rgba(255,255,255,0.08);
padding: 40px;
border-radius: 20px;
backdrop-filter: blur(12px);
box-shadow: 0px 10px 30px rgba(0,0,0,0.4);
}

h1 {
text-align:center;
color:#ffffff;
}

.stButton>button {
background: linear-gradient(45deg,#1DB954,#1ed760);
color:white;
border-radius:10px;
padding:10px 25px;
font-size:16px;
font-weight:bold;
border:none;
}

.stButton>button:hover {
background:#1DB954;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATA ---------------- #

moods = ['lovey dovey', 'happy', 'sad', 'lonely', 'travel']

mood_emojis = {
'lovey dovey':'💖',
'happy':'😄',
'sad':'😢',
'lonely':'😔',
'travel':'✈️'
}

languages = ['English', 'Hindi', 'Marathi', 'Punjabi', 'Korean']

song_types = [
'Pop',
'Romantic',
'Travel',
'Birthday Vibes',
'Wedding Vibes',
'Classical',
'Hip-Hop'
]

songs = {
'lovey dovey': {
'English': {'Romantic': ['Perfect - Ed Sheeran','All of Me - John Legend']},
'Hindi': {'Romantic': ['Tum Hi Ho','Raataan Lambiyan']},
'Marathi': {'Romantic': ['Yad Lagla','Sairat Zaala Ji']},
'Punjabi': {'Romantic': ['Khaab - Akhil']},
'Korean': {'Romantic': ['Sweet Night - V']}
},

'happy': {
'English': {'Pop': ['Happy - Pharrell Williams']},
'Punjabi': {'Pop': ['Born To Shine - Diljit Dosanjh']},
'Korean': {'Pop': ['Dynamite - BTS']}
},

'sad': {
'Hindi': {'Romantic': ['Channa Mereya']},
'Marathi': {'Romantic': ['Man Udhan Varyache']},
'Korean': {'Pop': ['Spring Day - BTS']}
},

'lonely': {
'English': {'Pop': ['Fix You - Coldplay']},
'Punjabi': {'Romantic': ['Soch - Hardy Sandhu']}
},

'travel': {
'Hindi': {'Travel': ['Ilahi']},
'Marathi': {'Travel': ['Morya Morya']},
'Korean': {'Travel': ['On The Ground - Rosé']}
}
}

# ---------------- UI ---------------- #

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.title("🎧 AI Mood-Based Playlist Generator")
st.write("Select your **mood, language, and song type** to get a recommendation.")

mood = st.selectbox("🎭 Select Mood", moods)

st.markdown(f"## {mood_emojis[mood]}")

language = st.selectbox("🌐 Select Language", languages)

song_type = st.selectbox("🎶 Select Song Type", song_types)

# ---------------- RECOMMEND SONG ---------------- #

if st.button("🎵 Generate Playlist"):

    try:

        song = random.choice(songs[mood][language][song_type])

        st.success(f"🎧 Recommended Song: **{song}**")

        query = urllib.parse.quote(song)
        spotify_url = f"https://open.spotify.com/search/{query}"

        st.markdown(f"[🎧 Listen on Spotify]({spotify_url})")

    except KeyError:

        st.error("❌ No song available for this selection.")

st.markdown("</div>", unsafe_allow_html=True)

st.write("---")
st.caption("Made with ❤️ ")