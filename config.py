from dotenv import load_dotenv
from os import environ

load_dotenv()
TEST_INPUT_AUDIO = environ.get("TEST_INPUT_AUDIO")
INPUT_AUDIO = environ.get("INPUT_AUDIO")
USE_MICROPHONE = environ.get("USE_MICROPHONE") in ["True", "true"]

SAMPLE_RATE = int(environ.get("SAMPLE_RATE"))
VOICE = environ.get("VOICE")
