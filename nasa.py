import os
import random
import requests
import speak as sp

def summary(body):
    list__ = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17')
    value = random.choice(list__)

    path = "C:\\Users\\Aysha Simra\\PycharmProject\\aiva\\NASA Img\\" + str(value) + ".jpg"
    os.startfile(path)

    name = str(body)
    url = "https://hubblesite.org/api/v3/glossary/" + name
    r = requests.get(url)
    Data = r.json()

    if len(Data) != 0:
        D = Data['definition']
        sp.speak(f"According To NASA {D}")
    else:
        sp.speak("No Data Available, Try Again Later!!")

if __name__ == "__main__":
    summary('earth')