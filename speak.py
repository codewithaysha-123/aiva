import pyttsx3
import speech_recognition as sr
from googletrans import Translator

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
    translate = Translator()
    result = translate.translate(line, src='hi', dest='en')
    Text = result.text
    speak(f"Ma'am, Translation for this line {Text}")

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
    line = takeKannada()
    translate = Translator()
    result = translate.translate(line, src='kn', dest='en')
    Text = result.text
    speak(f"Ma'am, Translation for this line {Text}")

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
    line = takeTamil()
    translate = Translator()
    result = translate.translate(line, src='ta', dest='en')
    Text = result.text
    speak(f"Ma'am, Translation for this line {Text}")

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
    line = takeTelugu()
    translate = Translator()
    result = translate.translate(line ,src='te' ,dest='en')
    Text = result.text
    speak(f"Ma'am, Translation for this line {Text}")

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
    line = takeArabic()
    translate = Translator()
    result = translate.translate(line, src='ar', dest='en')
    Text = result.text
    speak(f"Ma'am, Translation for this line {Text}")

