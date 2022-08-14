import pywhatkit
import wikipedia
import speak as sp
from pywikihow import search_wikihow
from bing_image_downloader import downloader

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

    downloader.download(Query, limit=10, output_dir='dataset', adult_filter_off=True, force_replace=False,
                        timeout=60, verbose=True)
