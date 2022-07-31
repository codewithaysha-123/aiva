import pywhatkit
import wikipedia
import speak as sp
import GoogleImageScraper
from pywikihow import search_wikihow
import os

def GoogleSearch(term):
    query = term.replace("aiva", "")
    writeab = str(query)

    Query = str(writeab)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        sp.speak(how_to_func[0].summary)
    else:
        pywhatkit.search(Query)
        search = wikipedia.summary(Query, 2)
        sp.speak(f"According to your Search: {search}")

    GoogleImageScraper.download(query=Query, limit=5, arguments={'download_format': 'png'})



if __name__ == "__main__":
    GoogleSearch("")