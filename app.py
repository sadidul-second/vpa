from flask import Flask
import config
from flask import request
from main import get_audio_from_file, inference


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/chat', methods=["POST"])
def chat():
    audio = request.files['audio']
    context = request.files['context']
    # context = context.stream.read().decode("utf-8")
    # audio = get_audio_from_file(audio)
    # audio = request.get_json()['audio']
    # context = request.get_json()['context']
    # print(audio)
    # print(context)
    try:
        audio.save("uploads/audio.wav")
        context.save("uploads/context.txt")
        with open("uploads/context.txt") as context:
            context = context.read()
            audio = get_audio_from_file("uploads/audio.wav")
        # # audio = get_audio_from_file("uploads/audio.wav")
        wav, reply, prompt = inference(audio, context)
        return dict(wav=wav.tolist(), reply=reply["answer"], score=reply["score"], prompt=prompt)
    except ValueError as e:
        return dict(error=str(e))


if __name__ == '__main__':
    try:
        print('>>>>>>>>>>>>', config.ENV_NAME)
        if config.ENV_NAME == "develop":
            app.run(host="0.0.0.0", port=config.PORT, debug=True)
        else:
            app.run(host="0.0.0.0", port=config.PORT, debug=False)
    finally:
        pass
