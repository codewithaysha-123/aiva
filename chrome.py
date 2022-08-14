from keyboard import press_and_release
import webbrowser as web

def chrome(command):
    while True:
        query = command

        if 'new tab' in query:
            press_and_release('ctrl + t')

        elif 'close tab' in query:
            press_and_release('ctrl + w')

        elif 'new window' in query:
            press_and_release('ctrl + n')

        elif 'history' in query:
            press_and_release('ctrl + h')

        elif 'downloads' in query:
            press_and_release('ctrl + j')

        elif 'bookmark' in query:
            press_and_release('ctrl + d + enter')

        elif 'incognito' in query:
            press_and_release('ctrl + shift + n')

        elif 'switch tab' in query:
            tab = query.replace('switch tab',"")
            Tab = tab.replace("to","")
            num = Tab
            bb = f'ctrl + {num}'
            press_and_release(bb)

        elif 'open' in query:
            name = query.replace("open","")
            NameA = str(name)
            string = "https://www." + NameA + ".com"
            web.open(string)

        elif "home" in query:
            press_and_release('Alt + Home')

        elif 'close current tab' in query:
            press_and_release('ctrl + F4')

        elif 'close current window' in query:
            press_and_release('ctrl + shift')

        elif "minimize current window" in query:
            press_and_release('Alt + space + n')

        elif "maximize current window" in query:
            press_and_release('Alt + space + x')

        elif 'exit' in query:
            press_and_release('alt + f + x')
            break


