from keyboard import press_and_release
from keyboard import press
import speak


def windowsAuto(command):
    query = str(command)

    if 'home screen' in query:
        press_and_release('windows + m')

    elif 'minimize' in query:
        press_and_release('windows + m')

    elif 'show start' in query:
        press('windows')

    elif 'open setting' in query:
        press_and_release('windows + i')

    elif 'open search' in query:
        press_and_release('windows + s')

    elif 'screen shot' in query:
        press_and_release('windows + SHIFT + s')

    elif 'restore windows' in query:
        press_and_release('windows + SHIFT + M')

    else:
        speak.speak("Sorry, Ma'am No Command Found!")


if __name__ == "__main__":
    windowsAuto('show start')