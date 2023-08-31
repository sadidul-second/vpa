from flask import Flask
import config

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    try:
        print('>>>>>>>>>>>>', config.ENV_NAME)
        if config.ENV_NAME == "develop":
            app.run(host="0.0.0.0", port=config.PORT, debug=True)
        else:
            app.run(host="0.0.0.0", port=config.PORT, debug=False)
    finally:
        pass
