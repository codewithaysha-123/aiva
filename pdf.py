import PyPDF2
import pyautogui

import speak as sp
from pdf2docx import Converter

def pdf2docx():
    sp.speak("Say the name of the file you would like to convert")
    inputpath = pyautogui.prompt("Enter the correct File path:")

    sp.speak("Ma'am, file is been converted.")
    save =inputpath.split(".")
    docx_file = save[0] + ".docx"
    c = Converter(inputpath)
    c.convert(docx_file)

    c.close

    sp.speak("ma'am, file has been saved!!")

def readpdf():
    sp.speak("Ma'am, Which file should i read?")
    path = pyautogui.prompt("Enter the file path: ")

    # creating a pdf file object
    pdfFileObj = open(path, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    sp.speak(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    sp.speak(pageObj.extractText())

    # closing the pdf file object
    pdfFileObj.close()



