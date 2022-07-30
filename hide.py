import speak as sp
import os
def hide():
    sp.speak("Ma'am please tell me do you want to hide this folder or make it visible for everyone")
    condition = sp.takeCommand()
    if 'hide' in condition:
        os.system("attrib +h /s /d")
        sp.speak("Ma'am, all the files in this folder are now hidden...")

    elif 'visible' in condition:
        os.system("attrib -h /s /d")
        sp.speak("Ma'am, all the files in this folder are visible to everyone. i hope your are taking this decision on your own pace")

    elif 'leave it' in condition or 'leave for now' in condition:
        sp.speak("Ok ma'am")


