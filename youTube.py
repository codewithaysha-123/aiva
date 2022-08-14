import webbrowser as web
from time import sleep
from keyboard import press_and_release
from pyautogui import press, click, write
import speak as sp
import pywhatkit


def YouTube(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    sp.speak("This is what i Found your Search Ma'am!!")
    pywhatkit.playonyt(term)


def YouTubesc(term):
    query = str(term)
    while (True):
        if 'pause' in query:
            press_and_release('space bar')

        elif 'resume' in query:
            press_and_release('space bar')

        elif 'full screen ' in query:
            press_and_release('f')

        elif 'film screen' in query:
            press_and_release('t')

        elif 'skip' in query:
            press_and_release('l')

        elif 'back' in query:
            press_and_release('j')

        elif 'increase' in query:
            press_and_release('shift + .')

        elif 'decrease' in query:
            press_and_release('shift + ,')

        elif 'previous' in query:

            press_and_release('shift + p')

        elif 'next' in query:
            press_and_release('shift + n')

        elif 'search' in query:
            click(x=597, y=133)

            sp.speak("What should I Search Ma'am")
            sea = sp.takeCommand()
            write(sea)
            sleep(1)
            press('enter')
        elif 'mute' in query:
            press_and_release('m')

        elif 'unmute' in query:
            press_and_release('m')

        else:
            sp.speak('No Commands')


if __name__ == "__main__":
    YouTube("python")