import pyautogui
import yagmail
import smtplib
import speak as sp

def sendFile():
    sp.speak("Ma'am, Enter your Email and Password!!!")
    sender = input("Enter your email: ")
    password = pyautogui.password(text='Enter Password', title='Auth', default='', mask='*')
    sp.speak("Ma'am To whom should i send email...")
    receiver = input("Enter receiver email id: ")
    ccname = input("Enter cc: ")
    bccname = input("Enter bcc: ")
    sp.speak("Ma'am what should be the subject for this email?")
    sub = sp.takeCommand()
    sp.speak("Ma'am  what should i say")
    body = sp.takeCommand()
    filename = [r"D:\\Simra\\wallpaper\\images 3.jfif"]

    # initializing the server connection
    yag = yagmail.SMTP(user=sender, password=password)
    # sending the email
    yag.send(to=receiver, cc=ccname, bcc=bccname, subject=sub, contents=body, attachments=filename)


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com")
    server.ehlo()
    server.starttls()
    sp.speak("Ma'am, Enter Your Email and Password!!!")
    email = input("Enter your email: ")
    password = pyautogui.password(text='Enter Password', title='Auth', default='', mask='*')
    server.login(email, password)
    server.sendmail(email, to, content)
    server.close()

if __name__ == "__main__":
    sendEmail("mahigeeks@gmail.com","this is done by aiva")