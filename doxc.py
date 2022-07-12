from docx2pdf import convert
from speak import speak as sp
def doxc2pdf():
    sp.speak("Wait Ma'am, processing to convert!")
    input = input("Enter correct path of file to convert:")
    out = input.split(".")
    output = out[0] + ".pdf"
    convert(input,output)
    sp.speak("Ma'am, file has been converted.")
