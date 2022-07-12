import speak as sp
import psutil
import speedtest as sts

def bat():
    # To sense the battery percentage
    battery = psutil.sensors_battery()
    percentage = battery.percent

    sp.speak(f"Ma'am our system have {percentage} percent battery")
    if 'percentage >= 75':
        sp.speak("We have enough power to continue our work")
    elif 'percentage >= 40 and percentage < 75':
        sp.speak("We should connect our system to charging point to charge our battery")
    elif 'percentage >= 15 and percentage < 40':
        sp.speak("We don't have enough power to work, please connect to charging")
    else:
        sp.speak("We have very low power, please connect to charging the system will shutdown very soon")

def intsp():
    sp.speak("Wait Ma'am, Checking internet speed!!")

    # Calling Speedtest function to know the speed of the internet
    st = sts.Speedtest()

    # Download Speed
    dl = st.download()/(1024**2)

    # Uploading Speed
    up = st.upload()/(1024**2)

    sp.speak(f"We have {dl} MB per second downloading speed and {up} MB per second uploading speed")