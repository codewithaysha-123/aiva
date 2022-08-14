from datetime import datetime
import nasapy
import os
import pandas as pd
import urllib.request
from speak import *

def nasainfo():
    # Initialize Nasa class by creating an object:

    k = "qThsiw02eex0r7MozodNKD7xEQEpzExqiPt5j29s"
    nasa = nasapy.Nasa(key=k)

    # Get a list of dates:
    time = datetime.now()
    dates = pd.date_range(end=time, periods=5)

    # Empty list to store dictionary keys and values:
    data = []

    speak("Ma'am, Collecting the data!!")

    # Getting all the data:
    for d in dates:
        apod = nasa.picture_of_the_day(d, hd=True)

        if apod['media_type'] == 'image':
            if 'hdurl' in apod.keys():
                data.append({'date': apod['date'], 'title': apod['title'], 'hdurl': apod['hdurl']})

    # Path of the directory:
    image_dir = "NASA Img"

        # Retrieving the image:
    for img in data:
        # Creating title for image:
        title = img["date"] + "_" + img["title"].replace(" ", "_").replace(":", "_") + ".jpg"

        # Downloading the image:
        urllib.request.urlretrieve(img['hdurl'],os.path.join(image_dir, title))

    speak("Collected the images from Nasa!!")


if __name__ == "__main__":
    nasainfo()