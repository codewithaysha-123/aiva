from speak import speak
import win32com.client
import os

def pptx2pdf():
    speak("Wait Ma'am, Processing to convert...")
    in_file = input("Enter the path of file:")
    out_file = os.path.splitext(in_file)[0]
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    pdf = powerpoint.Presentations.Open(in_file)
    speak("Ma'am,file has been converted.")
    pdf.SaveAs(out_file,32)
    pdf.Close()
    powerpoint.Quit()

if __name__ == "__main__":
    pptx2pdf()