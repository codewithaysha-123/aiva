import pywhatkit
import wikipedia
import speak as sp
from pywikihow import search_wikihow

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

