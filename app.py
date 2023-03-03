import os
from flask import Flask, render_template, request
import pyaudio
import wave
import datetime
from modules.whisper import recognize_audio
from modules.gpt import general_info, clean_speech, extract

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')


chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100
output_dir = "recs/"

p = pyaudio.PyAudio()
frames = []

# CV info placeholders
bio = ""
name = ""
address = ""
phone = ""

education = []
experience = []
interests = []
languages = []
qualities = []
skills = []

def start_recording():
    global frames
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []
    while True:
        data = stream.read(chunk)
        frames.append(data)


def stop_recording():
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_dir, f"{now}.wav")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename


@app.route('/start', methods=['POST'])
def start():
    start_recording()
    return "Recording started"


@app.route('/stop', methods=['POST'])
def stop():
    stop_recording()
    return "Recording stopped"


# question pages
@app.route('/')
def home():
    return render_template('start.html')


# general info
@app.route('/general')
def general():
    return render_template('general_info.html')


@app.route('/general/send', methods=['POST'])
def general_post():
    recording_filename = stop_recording()
    recognized = recognize_audio(recording_filename)
    output = general_info(recognized)
    name = output[0]
    address = output[0]
    phone = output[0]


@app.route('/bio')
def bio():
    return render_template('bio.html')


@app.route('/bio/send', methods=['POST'])
def bio_post():
    recording_filename = stop_recording()
    recognized = recognize_audio(recording_filename)
    bio = clean_speech(recognized)


@app.route('/exp')
def exp():
    return render_template('experience.html')


@app.route('/exp/send', methods=['POST'])
def exp_post():
    recording_filename = stop_recording()
    recognized = recognize_audio(recording_filename)
    experience = extract(recognized, 'work and volunteering experience')


@app.route('/ed')
def ed():
    return render_template('education.html')


@app.route('/ed/send', methods=['POST'])
def ed_post():
    recording_filename = stop_recording()
    recognized = recognize_audio(recording_filename)
    education = extract(recognized, 'education and certificates')


@app.route('/skill')
def skill():
    return render_template('skills.html')


@app.route('/skill/send', methods=['POST'])
def skill_post():
    recording_filename = stop_recording()
    recognized = recognize_audio(recording_filename)
    skills = extract(recognized, 'skills')


@app.route('/interest')
def interest():
    return render_template('interests.html')


@app.route('/interest/send', methods=['POST'])
def interest_post():
    recording_filename = stop_recording()
    recognized = recognize_audio(recording_filename)
    interests = extract(recognized, 'interests and hobbies')


@app.route('/lang')
def lang():
    return render_template('languages.html')


@app.route('/lang/send', methods=['POST'])
def lang_post():
    recording_filename = stop_recording()
    recognized = recognize_audio(recording_filename)
    languages = extract(recognized, 'languages')


@app.route('/quality')
def quality():
    return render_template('qualities.html')


@app.route('/quality/send', methods=['POST'])
def quality_post():
    recording_filename = stop_recording()
    recognized = recognize_audio(recording_filename)
    qualities = extract(recognized, 'personal qualities')


@app.route('/final')
def final():
    print(name, address, phone)
    print(bio)
    print(education)
    print(skills)
    print(experience)
    print(interests)
    print(languages)
    print(qualities)

    return render_template('final.html')


@app.route('/final/data')
def download():
    return {
        'name': name,
        'address': address,
        'bio': bio,
        'education': education,
        'skills': skills,
        'experience': experience,
        'interests': interests,
        'languages': languages,
        'qualities': qualities
    }


if __name__ == '__main__':
    app.run(debug=True)
