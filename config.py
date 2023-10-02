from dotenv import load_dotenv
from os import environ

load_dotenv()
ENV_NAME = environ.get("ENV_NAME")
PORT = environ.get("PORT")

TEST_INPUT_AUDIO = environ.get("TEST_INPUT_AUDIO")
INPUT_AUDIO = environ.get("INPUT_AUDIO")
USE_MICROPHONE = environ.get("USE_MICROPHONE") in ["True", "true"]

SAMPLE_RATE = int(environ.get("SAMPLE_RATE"))
VOICE = environ.get("VOICE")

WHISPER_MODEL = environ.get("WHISPER_MODEL")
# WHISPER_MODEL = environ.get("WHISPER_MODEL")
WHISPER_MODEL_OUTPUT = environ.get("WHISPER_MODEL_OUTPUT")
WHISPER_MODEL_CHECKPOINT = environ.get("WHISPER_MODEL_CHECKPOINT")
WHISPER_MODEL_LANGUAGE = environ.get("WHISPER_MODEL_LANGUAGE")
DATASET_STT = environ.get("DATASET_STT")
TARGET_SAMPLING_RATE = int(environ.get("TARGET_SAMPLING_RATE"))

TEMP_AUDIO = environ.get("TEMP_AUDIO")
INVOCATION_CONTEXT_PATH = environ.get("INVOCATION_CONTEXT_PATH")
INVOCATION_AUDIO_PATH = environ.get("INVOCATION_AUDIO_PATH")

CHAT_ENGINE_MODEL_OUTPUT = environ.get("CHAT_ENGINE_MODEL_OUTPUT")
