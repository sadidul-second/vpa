from main import get_audio_from_file, inference
import json


if __name__ == '__main__':
    try:
        with open("uploads/context.txt") as context:
            context = context.read()
            audio = get_audio_from_file("uploads/audio.wav")
        wav, reply, prompt = inference(audio, context)
        with open("results/output.json", "w") as output:
            json.dump(dict(wav=wav.tolist(), reply=reply["answer"], score=reply["score"], prompt=prompt), output)
    except ValueError as e:
        print(json.dumps(dict(error=str(e))))
