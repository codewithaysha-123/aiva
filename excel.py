import pyautogui
from win32com import client
from speak import *

def exe2pdf():
    speak("Ma'am, fetching for processing!!")
    app = client.DispatchEx("Excel.Application")
    app.interactive = False
    app.Visible = False

    path = pyautogui.prompt("Enter the path of file:")

    workbook = app.Workbooks.Open(path)
    workbook.ActiveSheet.ExportAsFixedFormat(0, path)
    workbook.Close()

    speak("Ma'am, file is converted!!")

