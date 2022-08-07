
import speak as sp
from pdf2docx import Converter

def pdf2docx():
    sp.speak("Say the name of the file you would like to convert")
    inputpath = str(input("Enter the correct File path:"))

    sp.speak("Ma'am, file is been converted.")
    save =inputpath.split(".")
    docx_file = save[0] + ".docx"
    c = Converter(inputpath)
    c.convert(docx_file)

    c.close

    sp.speak("ma'am, file has been saved!!")




