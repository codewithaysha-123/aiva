import datetime
import winsound
import speak as sp


def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    altime = altime[24:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)

    Mireal = altime[3:5]
    Mireal = int(Mireal)

    sp.speak(f"Done, alarm is set for {Timing}")

    while True:
        if Mireal == datetime.datetime.now().hour:
            if Mireal == datetime.datetime.now().minute:
                sp.speak("Alarm is running")
                winsound.PlaySound('abc', winsound.SND_LOOP)

            elif Mireal < datetime.datetime.now().minute:
                break


if __name__ == "__main__":
    alarm("14:02 pm")