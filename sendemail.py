import yagmail
import smtplib
import speak as sp
import pwinput

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com")
    server.ehlo()
    server.starttls()
    email = input("Enter your email: ")
    password = pwinput.pwinput(prompt='Enter your password: ',mask='.')
    server.login(email,password)
    server.sendmail(email,to,content)
    server.close()

def sendFile():
    sender = input("Enter your email: ")
    password = pwinput.pwinput(prompt='Enter your password: ',mask='.')
    sp.speak("Ma'am To whom should i send email...")
    receiver = input("Enter receiver email id: ")
    sp.speak("Ma'am what should be the subject for this email?")
    sub = sp.takeCommand()
    sp.speak("Ma'am  what should i say")
    body = sp.takeCommand()
    filename = 'programming-and-problem-solving-with-java.pdf'

    # initializing the server connection
    yag = yagmail.SMTP(user=sender, password=password)
    # sending the email
    yag.send(to=receiver, subject=sub, contents=body, attachments=filename)
    print("Email sent successfully")