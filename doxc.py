import pyautogui
from docx2pdf import convert
from speak import speak

def doxc2pdf():
    speak("Wait Ma'am, processing to convert!")
    name = pyautogui.prompt("Enter correct path of file to convert:")
    out = name.split(".")
    output = out[0] + ".pdf"
    convert(name, output)
    speak("Ma'am, file has been converted.")



