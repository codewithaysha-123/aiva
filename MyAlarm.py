import datetime
import vlc
import speak as sp

def alarm(Timing):
    sp.speak("Ma'am done, Alarm is Set.")
    while True:
        altime = datetime.datetime.now()
        now = altime.strftime("%H:%M")

        if now == Timing:
            media = vlc.MediaPlayer('C:\\Users\\Aysha Simra\\PycharmProject\\aiva\Alarm-ringtone.mp3')
            media.play()

        elif now > Timing:
            break


if __name__ == "__main__":
    alarm("11:23")