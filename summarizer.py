from transformers import pipeline
import re

# Load BART as text-generation (stable & supported)
summarizer = pipeline(
    "text-generation",
    model="facebook/bart-large-cnn"
)


def clean_text(text: str) -> str:
    """Remove filler words and extra spaces"""
    text = re.sub(r"\s+", " ", text).strip()
    fillers = [
        "like", "you know", "i mean", "basically", "actually", "so yeah",
        "right", "okay", "umm", "uh", "so", "well"
    ]
    for f in fillers:
        text = re.sub(rf"\b{f}\b", "", text, flags=re.IGNORECASE)
    return text.strip()


def detect_type(text: str) -> str:
    """Detect content type for better summarization"""
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

    # Prompt engineering
    if text_type == "school_system":
        prompt = (
            "Summarize this like a project demo explanation. "
            "Be structured, concise, and highlight key features:\n\n"
        )

    elif text_type == "casual_conversation":
        prompt = (
            "Summarize this casual conversation in clear bullet points. "
            "Capture important ideas or emotions:\n\n"
        )

    elif text_type == "promotion":
        prompt = (
            "Summarize this promotional content by keeping only the core message "
            "and removing marketing fluff:\n\n"
        )

    else:
        prompt = "Summarize the main ideas clearly and concisely:\n\n"

    final_input = prompt + text

    # Generate summary
    output = summarizer(
        final_input,
        max_length=180,
        min_length=60,
        do_sample=False,
        truncation=True
    )

    return output[0]["generated_text"].replace(final_input, "").strip()
