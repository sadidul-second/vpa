import speech_recognition as sr
from banglaspeech2text import Speech2Text

stt = Speech2Text(model="base", use_gpu=True)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    output = stt.recognize(audio)

print(output)
