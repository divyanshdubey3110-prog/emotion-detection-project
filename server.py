"""
This module deploys the Emotion Detection application using Flask.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    """Analyze user text and return detected emotions."""
    text_to_analyse = request.args.get("textToAnalyze", "")

    response = emotion_detector(text_to_analyse)

    if response is None or response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy}, "
        f"and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)