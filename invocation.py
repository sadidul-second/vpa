import requests
import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

    response = requests.get("http://localhost:5000/")
    print(response.content)
