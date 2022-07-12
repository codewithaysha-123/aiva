import speak as sp
import sys


def passpro(inpas):
    passprotect = 'pr|ncess'
    passrec = str(inpas)
    if passrec == str(passprotect):
        sp.speak("Access Granted!!!")
        sp.speak("Welcome Back, Ma'am!!")
    else:
        sp.speak("Access Denied!!!")
        sys.exit()


