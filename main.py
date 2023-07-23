from stt import recognize
from qa import generate_response
from tts import speech_reply
from config import INPUT_AUDIO, VOICE


if __name__ == '__main__':
    import glob
    context = "বাংলাদেশ ও ভারতের অনেক বৃহৎ নদী পূর্ব থেকে পশ্চিমে প্রবাহিত হয়ে বঙ্গোপসাগরে পতিত হয়েছে।\
            তন্মধ্যে উত্তরদিক থেকে গঙ্গা, মেঘনা এবং ব্রহ্মপুত্র; দক্ষিণদিক থেকে মহানদী, গোদাবরী, কৃষ্ণা, ইরাবতী এবং কাবেরী নদী উল্লেখযোগ্য।\
            ৬৪ কিলোমিটারব্যাপী (৪০ মাইল) কৌম নদী সবচেয়ে ছোট নদী হিসেবে সরু খাল দিয়ে এবং ২,৯৪৮ কিলোমিটারব্যাপী (১,৮৩২ মাইল)\
            বিশ্বের ২৮তম দীর্ঘ নদী হিসেবে ব্রহ্মপুত্র নদ বাংলাদেশ, চীন, নেপাল ও ভারতের মধ্য দিয়ে প্রবাহিত হয়ে বঙ্গোপসাগরে মিলিত হয়েছে।\
            সুন্দরবন ম্যানগ্রোভ বনাঞ্চল গঙ্গা, ব্রহ্মপুত্র ও মেঘনা নদীর ব-দ্বীপকে ঘিরে গঠিত হয়েছে। মায়ানমারের (সাবেক বার্মা) ইরাওয়াদি (সংস্কৃত ইরাবতী)\
            নদীও এ উপসাগরে মিলিত হয়েছে এবং একসময় গভীর ও ঘন ম্যানগ্রোভ বনাঞ্চলের সৃষ্টি করেছিল।"

    for i in glob.glob(INPUT_AUDIO + "*.wav"):
        print(i)
        prompt = recognize(i)
        print(f"STT: {prompt}")
        QA_input = {'question': prompt, 'context': context}
        reply = generate_response(QA_input)
        print(f"reply: {reply}")
        speech_reply(reply["answer"], VOICE)
