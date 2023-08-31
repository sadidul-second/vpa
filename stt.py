import speech_recognition as sr
from banglaspeech2text import Speech2Text
from config import TEST_INPUT_AUDIO, USE_MICROPHONE, INPUT_AUDIO


stt = Speech2Text(model="base", use_gpu=True, framework="pt")
r = sr.Recognizer()

print("use microphone: ", USE_MICROPHONE)


def recognize(path=None):
    if USE_MICROPHONE or path is None:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
    else:
        with sr.WavFile(path) as source:
            audio = r.record(source)

    try:
        return stt.recognize(audio)
    except LookupError:
        return "Could not understand what you are saying"


if __name__ == '__main__':
    import glob

    if USE_MICROPHONE:
        recognize(None)
    else:
        for i in glob.glob(INPUT_AUDIO + "*.wav"):
            print(i)
            output = recognize(i)
            print(output)
