import datetime
import json
import subprocess
import time

import requests
import speech_recognition as sr
import sounddevice as sd
from config import SAMPLE_RATE, USE_MICROPHONE, INVOCATION_AUDIO_PATH, INVOCATION_CONTEXT_PATH
from main import play_audio
import numpy as np
from save_audio import record

sd.default.samplerate = SAMPLE_RATE
r = sr.Recognizer()


def invoke():
    endpoint = "http://localhost:5000/chat"

    multiple_files = [
        ('audio', ('audio.wav', open(INVOCATION_AUDIO_PATH, 'rb'))),
        ('context', ('context.txt', open(INVOCATION_CONTEXT_PATH, 'rb')))
    ]
    # print(get_audio_from_file(INVOCATION_AUDIO_PATH).get_wav_data().decode("utf-8"))
    # json = {"audio": get_audio_from_file(INVOCATION_AUDIO_PATH).get_wav_data().decode("utf-8"), "context": context}
    # print("hi")
    start = time.time()
    result = requests.post(endpoint, files=multiple_files)
    print("processing time:", datetime.timedelta(seconds=time.time() - start))

    result = result.json()
    if "error" in result.keys():
        # print(result["error"])
        return 0
    else:
        print(result["prompt"])
        print(result["reply"])
        print(result["score"])
        wav = np.array(result["wav"])
        play_audio(wav)
        return 1


def invoke_ssh():
    try:
        ip = "185.32.161.60"
        port = "42404"
        print("invoking ssh...")
        subprocess.run(
            ["scp", "-i", "~/runpodio", "-P", f"{port}", "uploads/context.txt", f"root@{ip}:uploads/context.txt"]
        )
        subprocess.run(
            ["scp", "-i", "~/runpodio", "-P", f"{port}", "uploads/audio.wav", f"root@{ip}:uploads/audio.wav"]
        )
        result = subprocess.run(
            ["ssh", f"root@{ip}", "-p", f"{port}", "-i", "~/runpodio", "python", "inference.py"]
        )
        subprocess.run(
            ["scp", "-i", "~/runpodio", "-P", f"{port}", f"root@{ip}:results/output.json", "results/output.json"]
        )

        # print("--" * 20)
        # result = result.decode("utf-8")
        # print(result)
        # print("--" * 20)
        # playsound("uploads/output.wav")
        with open("results/output.json") as output:
            print(json.load(output))
        return 1
    except Exception as e:
        return 0


if __name__ == '__main__':
    if USE_MICROPHONE:
        print("Say something...")

        while True:
            record(INVOCATION_AUDIO_PATH)
            t = invoke()
    else:
        invoke()

    # print(i)
    # au = get_audio_from_file(i).get_wav_data()
    # # print(au)
    # w, r, p = inference(au, c)
    # print(p)
    # print(r)
    # sd.play(w, blocking=True)
    # # print(c)
    # data = {"contex": c, 'somekey': 'somevalue'}
    # d = urllib.parse.urlencode(data, encoding='utf-8')r
    # # print(d)
    # # response = requests.post(endpoint, data=data, headers={'Content-Type': 'application/json'})
    # response = requests.post(endpoint, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    # print(response.content)
