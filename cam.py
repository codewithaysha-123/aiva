import cv2
from PIL import Image

import speak as sp
import pyautogui
import numpy as np
import time
from keyboard import press_and_release
import pytesseract

def camera():
    sp.speak("Ok ma'am, Opening Camera")
    cap = cv2.VideoCapture(0)
    while True:
        # To read the captured video
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitkey(50)
        if k==27:
            break
    cap.release()
    cv2.destroyAllWindows

def screen():
    sp.speak("Ma'am, please tell me the name for this screenshot file")
    name = sp.takeCommand()
    sp.speak("Please hold the screen for few seconds, I am taking screenshot")
    time.sleep(5)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    sp.speak("I am done ma'am, the screenshot is saved in our main folder.")

def recsc():
    sp.speak("Ma'am, tell me the name for this recording!!")
    name = sp.takeCommand()
    SCREEN_SIZE = tuple(pyautogui.size())
    resolution = (1920, 1080)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(name + '.avi', fourcc, 20.0, (SCREEN_SIZE))
    webcam = cv2.VideoCapture(0)

    while True:
        # Capture the screen
        img = pyautogui.screenshot()
        # Convert the image into numpy array
        img = np.array(img)
        # Convert the color space from BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        _, frame = webcam.read()
        # Finding the width, height and shape of our webcam image
        fr_height, fr_width, _ = frame.shape
        # setting the width and height properties
        img[0:fr_height, 0: fr_width, :] = frame[0:fr_height, 0: fr_width, :]
        # cv2.imshow('frame', img)
        # Write the frame into the file 'output.avi'
        out.write(img)
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording Stopped")
            break

def switwind():
    sp.speak("Ma'am, switching the windows...")
    press_and_release('alt + tab')

def imagetext():
    sp.speak("ma'am, wait for processing the image!!")
    im = Image.open("image.jpg")

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    text = pytesseract.image_to_string(im, lang='eng')
    sp.speak(text)


if __name__ == "__main__":
    imagetext()
