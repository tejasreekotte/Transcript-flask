from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from pydub import AudioSegment
import json
from deep_translator import GoogleTranslator
from googletrans import Translator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ''
    translate = ''
    lang=''
    if request.method == 'POST':
        print('POST request received!')
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            sound = AudioSegment.from_mp3(file)
            sound.export("transcript.wav", format="wav")
            audioFile = sr.AudioFile("transcript.wav")
            with audioFile as source:
                # convert mp3 file to wav
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            with open("output.txt", "w") as out:
                out.write(transcript)
            lang=request.form['language']
            print(lang)
            translate = GoogleTranslator(source='english', target=lang).translate_file("output.txt")
    return render_template('home.html', transcript=transcript, translate=translate)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
