import speak as sp
import os
from twilio.rest import Client

def calls():
    sp.speak("Wait Ma'am, Connecting the call...")
    account_sid = os.environ['ACa797da99267d532b097e52264bb96bce']
    auth_token = os.environ['447b8c40f645559b6866dc7cd6dc7d55']
    client = Client(account_sid, auth_token)

    message = client.calls \
        .create(
        twiml='<Response><Say>This is the second testing message from jarvis side...</Say></Response>',
        From_='+16203178863',
        To='+14142408447'
    )

    sp.speak(message.sid)

def mess():
    sp.speak("Ma'am what should i say...")
    msz = sp.takeCommand()

    # if account lost this id will help me account UgtZ6wAuFUqxmC_H3Iw8HNVWxvrKqp_WAI4q7ycg
    # if 2nd account lost id amPCh75RsCAFwTHW7hdv4FpqBQSzLJDT
    account_sid = os.environ["ACa797da99267d532b097e52264bb96bce"]
    auth_token = os.environ["447b8c40f645559b6866dc7cd6dc7d55"]
    client = Client(account_sid, auth_token)

    message = client.message \
        .create(
        body=msz,
        From_='+16203178863',
        To='+14142408447'
    )

    sp.speak(message.sid)
    sp.speak("Message has been sent.")

    sp.speak(message.sid)
    sp.speak("Message has been sent.")

