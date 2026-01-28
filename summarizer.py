from transformers import pipeline
import re

# Load BART as text-to-text generator
summarizer = pipeline(
    task="text2text-generation",
    model="facebook/bart-large-cnn"
)


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    fillers = [
        "like", "you know", "I mean", "basically", "actually", "so yeah",
        "right", "okay", "umm", "uh", "so", "well"
    ]
    for f in fillers:
        text = text.replace(f, "")
    return text


def detect_type(text: str) -> str:
    t = text.lower()

    if any(word in t for word in ["teacher", "student", "attendance", "admin", "dashboard"]):
        return "school_system"

    if any(word in t for word in ["hey", "bro", "dude", "friend", "talking"]):
        return "casual_conversation"

    if any(word in t for word in ["salary", "career", "platform", "course", "skills"]):
        return "promotion"

    return "general"


def summarize_text(text: str) -> str:
    text = clean_text(text)

    if len(text.split()) < 40:
        return "Text too short to summarize."

    text_type = detect_type(text)

    if text_type == "school_system":
        prompt = (
            "Summarize this like a project demo explanation. "
            "Keep it structured, concise, and highlight key features:\n\n"
        )

    elif text_type == "casual_conversation":
        prompt = (
            "Summarize this casual conversation in simple bullet points. "
            "Capture important points or emotions:\n\n"
        )

    elif text_type == "promotion":
        prompt = (
            "Summarize this promotional content by keeping only the core message "
            "and removing marketing fluff:\n\n"
        )

    else:
        prompt = "Summarize the main ideas clearly and concisely:\n\n"

    final_input = prompt +_
