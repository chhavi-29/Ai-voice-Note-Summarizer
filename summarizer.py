from transformers import pipeline
import re

# Load BART summarizer
summarizer = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)


def clean_text(text: str) -> str:
    """Basic cleanup of filler words + repeated phrases"""
    text = re.sub(r"\s+", " ", text).strip()
    fillers = [
        "like", "you know", "I mean", "basically", "actually", "so yeah",
        "right", "okay", "umm", "uh", "so", "well"
    ]
    for f in fillers:
        text = text.replace(f, "")
    return text

def detect_type(text: str) -> str:
    """Detects type of speech for better summarization"""
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
    text_type = detect_type(text)

    # Custom prompts based on type
    if text_type == "school_system":
        prompt = (
            "Summarize this like a project demo explanation. "
            "Keep it structured, concise, and highlight key features:"
        )

    elif text_type == "casual_conversation":
        prompt = (
            "Summarize this casual conversation in simple bullet points. "
            "Capture the important points or emotions:"
        )

    elif text_type == "promotion":
        prompt = (
            "Summarize this promotional content so it contains only the core message and removes marketing fluff:"
        )

    else:
        prompt = "Summarize the main ideas clearly and concisely:"

    final_input = prompt + "\n\n" + text

    # HuggingFace summarization
    summary = summarizer(
        final_input,
        max_length=150,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]
