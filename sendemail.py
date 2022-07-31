import yagmail
import smtplib
import speak as sp
import pwinput

def sendFile():
    sender = input("Enter your email: ")
    password = pwinput.pwinput(prompt='Enter your password: ', mask='.')
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
    email = input("Enter your email: ")
    password = pwinput.pwinput(prompt='Enter your password: ', mask='.')
    server.login(email, password)
    server.sendmail(email, to, content)
    server.close()

if __name__ == "__main__":
    sendEmail("mahigeeks","This is done by aiva nice to meet you")