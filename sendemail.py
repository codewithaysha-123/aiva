import pyautogui
import re
import yagmail
import smtplib
import speak as sp

def sendFile():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    sender = "your email"
    password = "your app password"
    sp.speak("Ma'am To whom should i send email...")
    receiver = pyautogui.prompt("Enter receiver email id: ")
    def em():
        if (re.fullmatch(regex, receiver)):
            pyautogui.alert("Valid Email")
            ccname = pyautogui.prompt("Enter cc: ")
            if (re.fullmatch(regex, ccname)):
                pyautogui.alert("Valid cc")
                bccname = pyautogui.prompt("Enter bcc: ")
                if (re.fullmatch(regex, bccname)):
                    pyautogui.alert("Valid bcc")
                    sp.speak("Ma'am what should be the subject for this email?")
                    sub = sp.takeCommand()
                    sp.speak("Ma'am  what should i say")
                    body = sp.takeCommand()
                    filename = 'D:\Simra\wallpaper\images.jfif'
                    # initializing the server connection
                    yag = yagmail.SMTP(user=sender, password=password)
                    # sending the email
                    yag.send(to=receiver, cc=ccname, bcc=bccname, subject=sub, contents=body, attachments=filename)
                else:
                    pyautogui.alert("Invalid bcc")
                    em()

            else:
                pyautogui.alert("Invalid cc")
                em()

        else:
            pyautogui.alert("Invalid Email")
            em()
    em()

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com")
    server.ehlo()
    server.starttls()
    email = "your email"
    password = "your app password"
    server.login(email, password)
    server.sendmail(email, to, content)
    server.close()
