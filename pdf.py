import subprocess
import PyPDF2
import speak as sp
from pdf2docx import Converter

def pdf_reader():
    sp.speak("Which pdf file should i read?")
    pdf = input("Enter File Path:")
    book = open(pdf, 'r')

    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    sp.speak(f"Total number of pages in this pdf {pages}")
    sp.speak("Ma'am, please enter the page number i have to read...")

    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    sp.speak(text)

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

def pdf2pptx():
    sp.speak("Wait Ma'am, processing to convert the file")
    input = input("Enter the path of file to convert:")
    subprocess.run(["pdf2pptx",input])
    sp.speak("Ma'am, File has been converted")


