import requests


def recognize_audio(filename):
    url = "https://whisper.lablab.ai/asr"
    payload = {}

    files = [('audio_file', (filename, open(filename, 'rb'), 'audio/mpeg'))]

    response = requests.request("POST", url, data=payload, files=files)
    return response.json()["text"]
