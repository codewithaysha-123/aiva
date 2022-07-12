from speak import speak as sp
import win32com.client
import os

def pptx2pdf():
    sp.speak("Wait Ma'am, processing to convert!")
    in_file = input("Enter the path of file:")
    out_file = os.path.splitext(in_file)[0]
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    pdf = powerpoint.Presentations.Open(in_file)
    sp.speak("Ma'am,file has been converted.")
    pdf.SaveAs(out_file,32)
    pdf.Close()
    powerpoint.Quit()