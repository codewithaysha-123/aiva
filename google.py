import pywhatkit
import wikipedia
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScrapper
import speak as sp
from pywikihow import search_wikihow
import os

def GoogleSearch(term):
    query = term.replace("aiva", "")
    query = query.replace("what is", "")
    query = query.replace("how to", "")
    query = query.replace("who is", "")
    query = query.replace("what do you mean by", "")
    query = query.replace(" ", "")
    writeab = str(query)

    search = open("C:\\Users\\Aysha Simra\\PycharmProject\\aiva\\Data.txt", "w")

    search.write(writeab)
    search.close()

    Query = str(term)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query,max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        sp.speak(how_to_func[0].summary)
    else:
        pywhatkit.search(Query)
        search = wikipedia.summary(Query, 2)
        sp.speak(f"According to your Search: {search}")


def GoogleImage():
    oo = open('C:\\Users\\Aysha Simra\\PycharmProject\\aiva\\Data.txt', 'rt')
    query = str(oo.read())
    oo.close()
    pppp = open('C:\\Users\\Aysha Simra\\PycharmProject\\aiva\\Data.txt', 'r+')
    pppp.truncate(0)
    pppp.close()

    webdriver = "C:\\Users\\Aysha Simra\\PycharmProject\\aiva\\chromedriver.exe"
    photos = "C:\\Users\\Aysha Simra\\PycharmProject\\aiva\\google photos\\"

    search_keys = [f'{query}']
    number = 10
    head = False
    max(1000, 1000)
    min(0, 0)

    for search_key in search_keys:
        image_search = GoogleImageScrapper(webdriver, photos, search_keys, number, head, min, max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)

    os.startfile(photos)



