import sys
from remember import *
from dictate import Notepad
from sendemail import *
from requests import get
from win10toast import ToastNotifier
import MyAlarm
from windows import windowsAuto
from calc import *
from cam import *
from chrome import chrome
from covid import *
from google import *
from intbat import *
from insta import *
from loctemp import *
from news import news
from password import passpro
from pdf import *
from whatsapp import *
from youTube import *
from pptx import *
from doxc import *
from excel import *
from nasa import *

# to wish
def wishMe():
    hour =int(datetime.now().hour)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning! it's {time}")
    elif hour > 12 and hour < 18:
        speak(f"Good Afternoon! it's {time}")
    else:
        speak(f"Good Evening! it's {time}")
    speak("I am Aiva Ma'am!! Please tell me how may i help you")


def TaskExe():
    toast = ToastNotifier()
    toast.show_toast("AIVA ", "The AIVA is Now Activated!!!", duration=5)
    pyautogui.press('esc')

    wishMe()

    # password verification
    speak("For doing further tasks you need to enter password!!")
    passprotect = pyautogui.password(text='Enter Password', title='Auth', default='', mask='*')
   
    passpro(passprotect)

    while True:

        # logic building tasks
        query = takeCommand()
        if 'command prompt' in query or 'cmd' in query:
            if 'open' in query:
                speak("Ok ma'am, opening command prompt")
                os.system("start cmd")
            elif 'close' in query:
                speak("Ok ma'am, closing command prompt")
                os.system("TASKKILL /F /IM cmd.exe")

        elif 'hello' in query or 'hi' in query:
            speak("Hello ma'am, may i help you with something...")

        elif 'how are you' in query:
            speak("I am fine what about you?")

        elif "i am fine" in query or "i am good" in query:
            speak("It\'s glad to hear that your fine...")

        elif "remember that" in query:
            rem()

        elif 'What do you remember' in query:
            remember()

        elif 'notepad' in query:
            if 'open' in query:
                speak("Ok ma'am, opening notepad")
                os.startfile("notepad.exe")
            elif 'close' in query:
                speak("Ok ma'am, closing notepad")
                os.system("TASKKILL /F /IM notepad.exe")

        elif 'calculator' in query:
            if 'open' in query:
                speak("Ok ma'am, opening calculator")
                os.startfile("calc.exe")
            elif 'close' in query:
                speak("Ok ma'am, closing calculator")
                os.system("TASKKILL /F /IM calculator.exe")

        elif "open" in query:
            site = re.search(r'open (.*)', query)
            speak("Ok ma'am, opening the site")
            print(f"Opening:{site.group(1)}.com")
            webbrowser.open(f"www.{site.group(1)}.com")

        elif 'chrome' in query:
            if 'open' in query:
                speak("Ok Ma'am, Opening Chrome")
                os.startfile('chrome.exe')
            elif 'close' in query:
                speak("Ok Ma'am, Closing Chrome")
                os.system("TASKKILL /F /IM chrome.exe")
            else:
                chrome(query)

        elif 'youtube' in query:
            speak("Ok Ma'am tell me, what should i do? ")
            YouTubesc(query)

        elif 'camera' in query:
            camera()

        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")

        elif 'send email' in query:
            try:
                def email():
                    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    to = pyautogui.prompt("Enter Sender email: ")
                    speak("what should i say")
                    content = takeCommand()
                    if (re.fullmatch(regex, to)):
                        pyautogui.alert("Valid Email")
                        sendEmail(to, content)
                        speak("Email has been sent...")

                    else:
                        pyautogui.alert("Invalid Email")
                        email()
                email()


            except Exception as e:
                speak("sorry ma'am i am not able to send email...")

        elif "send file" in query:
            try:
                sendFile()
                speak("Email has been sent with file...")

            except Exception as e:
                speak("sorry ma'am i am not able to send email...")

        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("aiva", "")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            speak(results)

        elif 'google search' in query:
            speak("Ma'am What should i search in Google")
            cm = takeCommand()
            speak("This is What i found on the Web!!")

            try:
                GoogleSearch(cm)
                speak("I have Downloaded some images too, i hope you love it!!")

            except:
                speak("No Proper Data Available!!")

        elif 'whatsapp message' in query:
            query = query.replace("send", "")
            query = query.replace("whatsapp message", "")
            query = query.replace("to", "")
            name = query
            speak(f"What's the Message for{name}?")
            mess = takeCommand()
            whatsmess(name, mess)
            speak(f"Ma'am, Message has been sent to{name}")

        elif 'whatsapp call' in query:
            query = query.replace("make ", "")
            query = query.replace("whatsapp call ", "")
            query = query.replace("to ", "")
            name = query
            speak(f"Ma'am, Making Call to {name}")
            whatscall(name)

        elif 'whatsapp video call' in query:
            query = query.replace("make ", "")
            query = query.replace("whatsapp video call ", "")
            query = query.replace("to ", "")
            name = query
            speak(f"Ma'am, Making Video Call to {name}")
            whatscall(name)

        elif 'play' in query:
            speak("Wait Ma'am, Opening the Best Videos For You!!!")
            YouTube(query)

        elif "you can sleep now" in query:
            speak("Thanks for using me ma'am, have a good day... you can call me any time")
            break

        elif 'switch the window' in query:
            switwind()

        elif 'tell me a news' in query:
            speak("Wait ma'am, i'm fetching the latest news....")
            news()

        elif "set alarm" in query:
            speak("Ma'am please tell me the time to set alarm in 24 hour format")
            tt = takeCommand()
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            MyAlarm.alarm(tt)

        elif 'tell me a joke' in query:
            jokesen()

        elif 'shutdown the system' in query:
            speak("Ok ma'am. shutting down the system.")
            os.system("shutdown /s /t 1")

        elif 'restart the system' in query:
            speak("Ok ma'am. restarting the system")
            os.system("shutdown /r /t 1")

        elif 'sleep the system' in query:
            speak("Ok ma'am. the system will be in sleep mode.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'logout from pc' in query:
            speak("Ok ma'am. logging out from the pc")
            os.system("shutdown -l")

        elif 'covid cases' in query or 'corona cases' in query:
            cases()

        elif 'where i am' in query:
            myloc()

        elif 'temperature' in query:
            temperature()

        elif 'battery' in query or 'power' in query:
            bat()

        elif 'instagram profile' in query or 'insta profile' in query:
            instadown()

        elif 'screen recording' in query:

            speak("Ma'am, screen will be recording in few seconds!!")

            recsc()

            speak("Ma'am, Done recording the screen!!")

        elif 'pdf to docx converter' in query:
            pdf2docx()

        elif 'docx to pdf converter' in query:
            doxc2pdf()

        elif 'pptx to pdf converter' in query:
            pptx2pdf()

        elif 'excel to pdf converter' in query:
            exe2pdf()

        elif 'calculate' in query:
            calculate()

        elif 'take a screenshot' in query:
            screen()

        elif 'convert image to text' in query:
            speak("Wait ma'am, processing to fetch image for conversion!!")
            imagetext()

        elif 'where is' in query:
            place = query.replace("where is", "")
            place = place.replace("aiva", "")
            GoogleMaps(place)

        elif 'windows' in query:
            command = query.replace("windows", "")
            command = command.replace("aiva", "")
            windowsAuto(command)

        elif 'make notes' in query:
            Notepad()

        elif 'nasa' in query:
            nasainfo()

        elif 'read pdf' in query:
            readpdf()

        elif 'goodbye' in query:
            speak("Thanks for Using Me Ma'am, have a great day...")
            toast = ToastNotifier()
            toast.show_toast("Aiva", "The Aiva is Now Deactivated!!!", duration=5)
            sys.exit()

if __name__ == "__main__":
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    recognizer.read('trainer/trainer.yml')  
    cascadePath = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)  

    font = cv2.FONT_HERSHEY_SIMPLEX  

    id = 2  

    names = ['', 'aysha']  

    camer = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
    camer.set(3, 640)  
    camer.set(4, 480)  

    minW = 0.1 * camer.get(3)
    minH = 0.1 * camer.get(4)

    # flag = True

    while True:

        ret, img = camer.read()  

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  

            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  

            if (accuracy < 100):
                accuracy = "  {0}%".format(round(100 - accuracy))
                permission = takeCommand()
                if "wake up" in permission:
                    TaskExe()

                elif 'goodbye' in permission:
                    speak("Thanks for Using Me Ma'am, have a great day...")
                    toast = ToastNotifier()
                    toast.show_toast("Aiva", "The Aiva is Now Deactivated!!!", duration=5)
                    sys.exit()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("Unauthorized Access!!")
                sys.exit()

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  
        if k == 13:
            break

    print("Thanks for using this program, have a good day.")
    camer.release()
    cv2.destroyAllWindows()
