import pyttsx3
import speech_recognition as sr
from translate import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Commands
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=10, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")

        except Exception as e:
            return "None"
        query = query.lower()
        return query

def takeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"User said: {query}")

    except Exception as e:
        return "None"
    query = query.lower()
    return query

def transhin():
    speak("Ma'am, Tell me the line!!")
    line = takeHindi()
    translate = Translator(from_lang="hindi",to_lang="english")
    result = translate.translate(line)
    speak(f"Ma'am, Translation for this line {result}")

def takeKannada():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='kn')
        print(f"User said: {query}")

    except Exception as e:
        return "None"
    query = query.lower()
    return query

def transkann():
    speak("Ma'am, Tell me the line!!")
    line = takeHindi()
    translate = Translator(from_lang="kannada", to_lang="english")
    result = translate.translate(line)
    speak(f"Ma'am, Translation for this line {result}")

def takeTamil():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='ta')
        print(f"User said: {query}")

    except Exception as e:
        return "None"
    query = query.lower()
    return query

def tranTamil():
    speak("Ma'am, Tell me the line!!")
    line = takeHindi()
    translate = Translator(from_lang="tamil", to_lang="english")
    result = translate.translate(line)
    speak(f"Ma'am, Translation for this line {result}")

def takeTelugu():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='te')
        print(f"User said: {query}")

    except Exception as e:
        return "None"
    query = query.lower()
    return query

def tranTelugu():
    speak("Ma'am, Tell me the line!!")
    line = takeHindi()
    translate = Translator(from_lang="telugu", to_lang="english")
    result = translate.translate(line)
    speak(f"Ma'am, Translation for this line {result}")

def takeArabic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='ar')
        print(f"User said: {query}")

    except Exception as e:
        return "None"
    query = query.lower()
    return query

def tranArabic():
    speak("Ma'am, Tell me the line!!")
    line = takeHindi()
    translate = Translator(from_lang="Arabic", to_lang="english")
    result = translate.translate(line)
    speak(f"Ma'am, Translation for this line {result}")

if __name__ == "__main__":
    transhin()