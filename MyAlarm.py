import datetime
from playsound import playsound #pip install playsound==1.2.2
import speak as sp

def alarm(Timing):
    sp.speak("Ma'am done, Alarm is Set.")
    while True:
        altime = datetime.datetime.now()
        now = altime.strftime("%H:%M")

        if now == Timing:
            playsound("https://notificationsounds.com//storage/sounds/file-a1_ascendent-64kbps.mp3")

        elif now > Timing:
            break




