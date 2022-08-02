from datetime import datetime
import nasapy
import os
import pandas as pd
import urllib.request
from IPython.display import Image,display
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

    speak("Still processing please wait for few minutes...")

    # Get a list of images:
    astro_images = os.listdir(image_dir)

    # Displaying an image:
    Image(os.path.join(image_dir, astro_images[0]))

    # Get random image:
    import random
    Image(os.path.join(image_dir, astro_images[random.randint(0, len(astro_images) - 1)]))
    speak("Ma'am wait fetching the images!!")

if __name__ == "__main__":
    nasainfo()