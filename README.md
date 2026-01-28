

# AI Voice Note Summarizer

## Overview

The AI Voice Note Summarizer is a speech-to-text and natural language processing application designed to convert audio recordings into structured and concise summaries. The application addresses the common challenge of reviewing long voice notes by automatically transcribing and summarizing spoken content.

This project demonstrates the practical integration of speech recognition models with transformer-based prompt-driven text generation techniques and is deployed as a web application for real-world usability.

---

## Live Application

The application is deployed and accessible at:
[https://ai-voice-note-summarizer-chhavi.streamlit.app/](https://ai-voice-note-summarizer-chhavi.streamlit.app/)

---

## Problem Statement

Voice notes are widely used for communication, meetings, and quick idea capture. However, reviewing long audio recordings is inefficient and time-consuming. Manually extracting key points from audio requires repeated listening and note-taking.

This project provides an automated solution that converts spoken content into readable text and generates concise summaries, improving productivity and information accessibility.

---

## Solution

The application processes uploaded audio files through an end-to-end AI pipeline:

1. Converts speech into text using a speech recognition model
2. Cleans and analyzes the transcribed text
3. Detects the conversational context of the speech
4. Generates concise summaries using prompt-based transformer text generation

The system is designed to handle multiple types of speech, including casual conversations, project explanations, and informational or promotional content.

---

## Key Features

* Upload and process common audio formats (mp3, wav, m4a, mpeg)
* Speech-to-text transcription using Whisper
* Prompt-based transformer text generation for summarization
* Adaptive summarization logic based on detected conversation type
* Clean and minimal web interface
* Cloud deployment for public accessibility

---

## Technology Stack

* **Python**
* **Streamlit** – Application interface and cloud deployment
* **OpenAI Whisper** – Speech recognition
* **Hugging Face Transformers (BART)** – Prompt-based text generation for summarization
* **PyTorch** – Model execution backend
* **FFmpeg** – Audio preprocessing

---

## System Architecture

1. User uploads an audio file through the web interface
2. Whisper transcribes the audio into text
3. The text is cleaned and analyzed to determine its context
4. A transformer-based text generation model produces a concise summary using contextual prompts
5. Both transcription and summary are displayed to the user

---

## Project Structure

```
ai-voice-note-summarizer/
│
├── app.py              # Streamlit application
├── summarizer.py       # Custom summarization logic
├── background.png      # UI background asset
├── requirements.txt    # Python dependencies
├── packages.txt        # System-level dependencies (ffmpeg)
└── README.md
```

---

## Deployment

The application is deployed using Streamlit Cloud.

### Deployment Steps

1. Source code hosted on GitHub
2. Python dependencies managed using `requirements.txt`
3. System dependency (ffmpeg) installed using `packages.txt`
4. Application deployed directly from the GitHub repository using Streamlit Cloud

---

## Running Locally

To run the application locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Ensure that `ffmpeg` is installed and available in the system path.

---

## Learning Outcomes

* Practical implementation of speech-to-text pipelines
* Experience with transformer-based text generation models
* Understanding prompt engineering for controlled summarization
* Debugging and resolving cloud deployment issues
* Building and deploying end-to-end AI systems

---

## Future Enhancements

* Export summaries as downloadable files
* Support for real-time voice recording
* Multi-language transcription and summarization
* User authentication and summary history tracking




