import datetime
import os
from speak import *

def Notepad():
    speak("Ma'am, tell me the query!!")
    speak("I am ready to Write!!")
    writes = takeCommand()
    time = int(datetime.now().strftime("%H:%M"))
    filename = str(time) + "-note.txt"
    with open(filename,"w") as file:
        file.write(writes)

    path_1 = "C:\\Users\\Aysha Simra\\PycharmProject\\aiva\\notes\\" + str(filename)
    path_2 = "D:\\python project\\notepad\\" + str(filename)

    os.rename = (path_1,path_2)
    os.startfile(path_2)