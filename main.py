import numpy

from stt import recognize
from qa import generate_response
from tts import speech_reply
from config import INPUT_AUDIO, VOICE
# from whisper import recognize
import sounddevice as sd
from config import SAMPLE_RATE
import speech_recognition as sr
from config import USE_MICROPHONE

sd.default.samplerate = SAMPLE_RATE
rec = sr.Recognizer()


def inference(audio, context):
    prompt = recognize(audio)
    QA_input = {'question': prompt, 'context': context}
    reply = generate_response(QA_input)
    wave = speech_reply(reply["answer"], VOICE)
    return wave, reply, prompt


def get_audio_from_mic():
    with sr.Microphone() as source:
        audio = rec.listen(source)

    return audio


def get_audio_from_file(path):
    with sr.WavFile(path) as source:
        audio = rec.record(source)

    return audio


def play_audio(wav):
    sd.play(wav, blocking=True)


if __name__ == '__main__':
    c = """আগামী অক্টোবর থেকে থেকে শুরু হতে যাওয়া মৌসুমে ভারত চিনি রপ্তানি নিষিদ্ধ করতে পারে। ভারতের ৩টি সরকারি 
    সূত্রের বরাত দিয়ে এ তথ্য জানিয়েছে বার্তা সংস্থা রয়টার্স।

    রয়টার্সের প্রতিবেদনে বলা হয়েছে, বৃষ্টির অভাবে আখের ফলন কমে যাওয়ায় গত ৭ বছরের মধ্যে প্রথমবারের মতো রপ্তানি 
    বন্ধের পরিকল্পনা করছে ভারত।

    ভারত চিনি রপ্তানি বন্ধ করলে বিশ্ব বাজারে, যেমন নিউইয়র্ক ও লন্ডনে চিনির দাম আরও বাড়তে পারে এবং বিশ্বব্যাপী খাদ্য 
    বাজারে আরও মূল্যস্ফীতির আশঙ্কা তৈরি করবে। ইতোমধ্যে কয়েক বছর ধরে চিনির দাম বেড়েছে।

    নাম প্রকাশে অনিচ্ছুক একটি সরকারি সূত্র রয়টার্সকে জানিয়েছে, 'আমাদের প্রাথমিক লক্ষ্য স্থানীয় বাজারে চিনির চাহিদা 
    পূরণ করা এবং উদ্বৃত্ত আখ থেকে ইথানল উত্পাদন করা। তাই আগামী মৌসুমে রপ্তানি করার মতো পর্যাপ্ত চিনি আমাদের কাছে 
    থাকবে না।'

    চলতি মৌসুমের ৩০ সেপ্টেম্বর পর্যন্ত মাত্র ৬১ লাখ টন চিনি রপ্তানির অনুমতি দিয়েছিল ভারত। অথচ, গত মৌসুমে রেকর্ড ১১ 
    দশমিক ১ মিলিয়ন টন চিনি বিক্রি করেছিল দেশটি।"""
    import glob

    # if USE_MICROPHONE is None:
    #     with sr.Microphone() as source:
    #         print("Say something!")
    #         audio = r.listen(source)
    # else:
    #     with sr.WavFile(path) as source:
    #         audio = r.record(source)
    if USE_MICROPHONE:
        while True:
            try:
                au = get_audio_from_mic()
                w, r, p = inference(au, c)
                print("Question:", p)
                print("Answer:", r["answer"])
                print("Confidence:", r["score"])
                play_audio(w)
            except ValueError:
                pass
    else:
        for i in glob.glob(INPUT_AUDIO + "*.wav"):
            print(i)
            au = get_audio_from_file(i)
            w, r, p = inference(au, c)
            print(p)
            print(r)
            play_audio(numpy.array(w.tolist()))
            # sd.play(w, blocking=True)
