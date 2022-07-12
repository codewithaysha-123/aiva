import cv2
import speak as sp
import pyautogui
import numpy as np
import time
from PIL import Image
import pytesseract

def camera():
    sp.speak("Ok ma'am, Opening Camera")
    cap = cv2.VideoCapture(0)
    # To read the captured video
    ret, img = cap.read()
    cv2.imshow('webcam', img)
    query = sp.takeCommand()
    if 'quit' in query:
        sp.speak("Ok Ma'am,Closing Camera")
        # the captured video is released
        cv2.release()

        # destroys all the windows
        cv2.destroyAllwindows()


def screen():
    sp.speak("Ma'am, please tell me the name for this screenshot file")
    name = sp.takeCommand()
    sp.speak("Please ma'am hold the screen for few seconds, i am taking screenshot")
    time.sleep(5)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    sp.speak("I am done ma'am, the screenshot is saved in our main folder.")

def recsc():
    # Create VideoWriter Object
    resolution = pyautogui.size()
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "Recording.avi"
    fps = 60.0
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # Create Window to show live Recording
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)

    # Infinite loop for record screen
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.imshow("Live", frame)
        if cv2.waitKey(1) == ord('q'):
            break

def switwind():
    sp.speak("Ma'am, switching the windows...")
    pyautogui.keyDown('alt')
    pyautogui.keyUp('tab')
    time.sleep(1)
    pyautogui.keyUp('alt')

def imagetext():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    image = input("Enter image path for conversion:")
    img_1 = Image.open(image,'r')
    text = pytesseract.image_to_string(img_1)
    sp.speak(text)

