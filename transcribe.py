import speech_recognition as sr
from os import path
from pydub import AudioSegment
import json
from deep_translator import GoogleTranslator
from googletrans import Translator
# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("Rev.mp3")
sound.export("transcript.wav", format="wav")

# transcribe audio file                                                         
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        #print("Transcription: " + r.recognize_google(audio))
        a=r.recognize_google(audio)
        #print(a)
        with open("my_output_file.txt", "w") as out:
            out.write(a)
            
translated = GoogleTranslator(source='english', target='german').translate_file("my_output_file.txt")
print(translated)       