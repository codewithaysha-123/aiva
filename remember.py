from speak import *
import pyjokes

def rem():
    query = takeCommand()
    rememberMsg = query.replace("remember that", "")
    speak("Ma'am, you tell me To remind that" + rememberMsg)
    remember = open('Data.txt', 'w')
    remember.write(rememberMsg)
    remember.close()

def remember():
    remember = open('Data.txt', 'r')
    speak("Ma'am, you told me that" + remember.read())
    remember.close()

def jokesen():
    speak("Ok ma'am please wait searching the jokes to say...")
    jokes = pyjokes.get_joke(language='en', category='neutral')
    speak(jokes)

