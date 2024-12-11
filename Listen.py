import speech_recognition as sr 
from googletrans import Translator

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")

    except:
        return ""

    query = str(query).lower()
    return query

def TranslationHinToEng(Text):
    line = str(Text)
    # Using the Google Translate API to translate the text
    try:
        translate = Translator()
        result = translate.translate(line)
        data = result.text
        print(f"You : {data}.")
        return data
    except Exception as e:
        print("Translation error:", e)
        return None

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data
