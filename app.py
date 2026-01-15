import streamlit as st
import whisper
import tempfile
from summarizer import summarize_text

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Voice Note Summarizer",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>

    /* Remove Streamlit default header & top purple block */
    header, footer {visibility: hidden;}
    .stApp > header {display: none;}

    /* Background image */
    .stApp {
        background: url("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4") no-repeat center center fixed;
        background-size: cover;
    }

    /* Main container */
    .block-container {
        background: rgba(0, 0, 0, 0.35);
        border-radius: 20px;
        padding: 40px;
        margin-top: 30px;
    }

    /* Make all text white */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: white !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: black;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: 1px solid white;
    }

    /* File uploader */
    .stFileUploader {
        background: rgba(255,255,255,0.15);
        border-radius: 12px;
        padding: 10px;
    }

    /* Audio player */
    audio {
        width: 100%;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD MODELS ----------------
@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

model = load_whisper()

# ---------------- UI ----------------
st.title("🎙️ Voice Note Summarizer")
st.write("Upload an audio file to get transcription and intelligent summary.")

audio_file = st.file_uploader(
    "Choose an audio file",
    type=["mp3", "wav", "m4a", "mpeg"]
)

if audio_file:
    st.audio(audio_file)

    if st.button("Summarize"):
        with st.spinner("Processing audio..."):

            # Save temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_file.read())
                tmp_path = tmp.name

            # Transcription
            result = model.transcribe(tmp_path)
            transcription = result["text"]

            # Summary
            summary = summarize_text(transcription)

        # ---------------- OUTPUT ----------------
        st.subheader("📝 Transcription")
        st.write(transcription)

        st.subheader("📌 Summary")
        st.write(summary)
