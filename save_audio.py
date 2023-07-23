import sounddevice as sd
import wavio as wv
from config import TEST_INPUT_AUDIO, INPUT_AUDIO, SAMPLE_RATE
from stt import recognize


def record(path, duration=3, freq=44100):
    # Start recorder with the given values of
    # duration and sample frequency
    path = path or TEST_INPUT_AUDIO
    print("Say something...")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    wv.write(path, recording, freq, sampwidth=2)
    print(f"saved: {path}")


if __name__ == '__main__':
    file_path = INPUT_AUDIO + "brammaputra-river-lenth.wav"
    record(file_path, duration=3, freq=SAMPLE_RATE)
    recognize(file_path)
