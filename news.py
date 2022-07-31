import requests
import speak as sp

def news():
    query_params = {
        "source":"bbc-news",
        "sortby":"top",
        "apikey":"425675b8ff12423487e9e81200646ea4"
    }
    main_url = "https://newsapi.org/v1/articles"
    main_page = requests.get(main_url,query_params).json()
    article = main_page["articles"]
    head = []

    for ar in article:
        head.append(ar["title"])

    for i in range(len(head)):
        sp.speak(f"{i+1}.{head[i]}")

if __name__ == "__main__":
    news()