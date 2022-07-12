from win32com import client
from speak import speak as sp

def exe2pdf():
    sp.speak("Ma'am, fetching for processing!!")
    app = client.DispatchEx("Excel.Application")
    app.interactive = False
    app.Visible = False

    path = input("Enter the path of file:")

    workbook = app.Workbooks.Open(path)
    workbook.ActiveSheet.ExportAsFixedFormat(0, path)
    workbook.Close()

    sp.speak("Ma'am, file is converted!!")