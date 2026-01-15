

# AI Voice Note Summarizer

## Overview

The AI Voice Note Summarizer is a speech-to-text and natural language processing application designed to convert audio recordings into structured and concise summaries. The application addresses the common challenge of reviewing long voice notes by automatically transcribing and summarizing spoken content.

This project demonstrates the practical integration of speech recognition models with transformer-based NLP techniques and is deployed as a web application for real-world usability.

---
## Live Application

The application is deployed and accessible at:
https://ai-voice-note-summarizer-chhavi.streamlit.app/
---

## Problem Statement

Voice notes are widely used for communication, meetings, and quick idea capture. However, reviewing long audio recordings is inefficient and time-consuming. This project provides an automated solution to extract meaningful information from voice recordings in a readable and structured format.

---

## Solution

The application processes uploaded audio files through an end-to-end AI pipeline:

1. Converts speech into text
2. Cleans and analyzes the text
3. Generates concise summaries tailored to the type of conversation

The system is designed to handle different forms of speech, including casual conversations, presentations, and informational or promotional content.

---

## Key Features

* Upload and process common audio formats (`mp3`, `wav`, `m4a`, `mpeg`)
* Speech-to-text transcription using Whisper
* Transformer-based text summarization
* Adaptive summarization logic based on detected conversation type
* Clean and minimal web interface
* Cloud deployment for public accessibility

---

## Technology Stack

* **Python**
* **Streamlit** – Application interface and deployment
* **OpenAI Whisper** – Speech recognition
* **Hugging Face Transformers (BART)** – Text summarization
* **PyTorch** – Model execution
* **FFmpeg** – Audio preprocessing

---

## System Architecture

1. User uploads an audio file via the web interface
2. Whisper transcribes the audio into text
3. Text is cleaned and analyzed to determine its context
4. A transformer-based summarization model generates a concise summary
5. Transcription and summary are displayed to the user

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

Deployment steps:

1. Source code hosted on GitHub
2. Python dependencies managed using `requirements.txt`
3. System dependency (`ffmpeg`) installed using `packages.txt`
4. Application deployed directly from the GitHub repository

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
* Experience with transformer-based NLP models
* Understanding of AI application deployment workflows
* Debugging and resolving cloud deployment issues
* Building end-to-end AI systems

---

## Future Enhancements

* Export summaries as downloadable files
* Support for real-time voice recording
* Multi-language transcription and summarization
* User authentication and summary history



