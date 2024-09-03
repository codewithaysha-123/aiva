from datetime import datetime
import nasapy
import os
import pandas as pd
import requests
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

    image_dir = "NASA Img"

    for img in data:
        title = img["date"] + "_" + img["title"].replace(" ", "_").replace(":", "_") + ".jpg"

        response = requests.get(img['hdurl'], stream=True)  # Use stream for larger images

        if response.status_code == 200:
            with open(os.path.join(image_dir, title), 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded {title} successfully!")
        else:
            print(f"Failed to download {title} (status code: {response.status_code})")
    speak("Collected the images from Nasa!!")


