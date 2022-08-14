import pyautogui

import speak as sp
import webbrowser
import time
import instaloader as insta

def instadown():
    sp.speak("Ma'am please enter the username correctly...")
    name = pyautogui.prompt("Enter username here: ")

    webbrowser.open(f"www.instagram.com/{name}")
    sp.speak("Ma'am here is the profile of the user {name}")
    time.sleep(5)

    sp.speak("Would you like to download picture of this account.")
    condition = sp.takeCommand()
    if "yes" in condition:
        # Load the profile picture
        mod = insta.Instaloader()

        # Save or Download the insta pic
        mod.download_profile(name, profile_pic_only=True)
        sp.speak("I am done ma'am, profile picture is saved...")
    else:
        pass


