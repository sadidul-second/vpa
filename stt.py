from banglaspeech2text import Speech2Text
from config import USE_MICROPHONE, INPUT_AUDIO


stt = Speech2Text(model="base", use_gpu=True, framework="pt")


def recognize(audio):
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
