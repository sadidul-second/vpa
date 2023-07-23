from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "Naimul/banglabert-finetuned-squad"

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
QA = pipeline('question-answering', model=model, tokenizer=tokenizer)


def generate_response(prompt):
    return QA(prompt)


if __name__ == '__main__':
    context = "বাংলাদেশ ও ভারতের অনেক বৃহৎ নদী পূর্ব থেকে পশ্চিমে প্রবাহিত হয়ে বঙ্গোপসাগরে পতিত হয়েছে।\
    তন্মধ্যে উত্তরদিক থেকে গঙ্গা, মেঘনা এবং ব্রহ্মপুত্র; দক্ষিণদিক থেকে মহানদী, গোদাবরী, কৃষ্ণা, ইরাবতী এবং কাবেরী নদী উল্লেখযোগ্য।\
    ৬৪ কিলোমিটারব্যাপী (৪০ মাইল) কৌম নদী সবচেয়ে ছোট নদী হিসেবে সরু খাল দিয়ে এবং ২,৯৪৮ কিলোমিটারব্যাপী (১,৮৩২ মাইল)\
    বিশ্বের ২৮তম দীর্ঘ নদী হিসেবে ব্রহ্মপুত্র নদ বাংলাদেশ, চীন, নেপাল ও ভারতের মধ্য দিয়ে প্রবাহিত হয়ে বঙ্গোপসাগরে মিলিত হয়েছে।\
    সুন্দরবন ম্যানগ্রোভ বনাঞ্চল গঙ্গা, ব্রহ্মপুত্র ও মেঘনা নদীর ব-দ্বীপকে ঘিরে গঠিত হয়েছে। মায়ানমারের (সাবেক বার্মা) ইরাওয়াদি (সংস্কৃত ইরাবতী)\
    নদীও এ উপসাগরে মিলিত হয়েছে এবং একসময় গভীর ও ঘন ম্যানগ্রোভ বনাঞ্চলের সৃষ্টি করেছিল।"
    question = "ব্রহ্মপুত্র নদের মোট দৈর্ঘ্য কত ?"

    QA_input = {'question': question, 'context': context}
    response = generate_response(QA_input)
    print(response)
