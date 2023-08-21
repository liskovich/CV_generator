import os
import openai
from dotenv import load_dotenv

if os.getenv("OPENAI_KEY") is None:
    load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

def clean_speech(voice_input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Correct grammar and vocabulary errors in this text, and make it more formal: {voice_input}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text


def extract(voice_input, keyword):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract all mentioned {keyword} from this text, and return list of that separated by commas: {voice_input}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    line = response.choices[0].text
    return line.split(",")


def general_info(voice_input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract person's name, address and phone number from this text, and return them in form name,address,phone: {voice_input}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    line = response.choices[0].text
    return line.split(",")

# export OPENAI_API_KEY=sk-...
