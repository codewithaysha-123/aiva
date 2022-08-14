from speak import *

def Notepad():
    speak("Ma'am, tell me the query!!")
    speak("I am ready to Write!!")
    writes = takeCommand()
    speak("Ma'am, tell me the name for this file!!!!")
    time = takeCommand()
    filename = str(time) + "-note.txt"
    with open(filename, "w") as file:
        file.write(writes)