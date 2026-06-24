"""Emotion detection module using Watson NLP."""

import json
import requests
from requests.exceptions import RequestException

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADER = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def empty_response():
    """Return an empty emotion response."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }


def emotion_detector(text_to_analyse):
    """Detect emotions in the given text."""
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(
            URL,
            json=input_json,
            headers=HEADER,
            timeout=30
        )
    except RequestException:
        return empty_response()

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }

    return empty_response()