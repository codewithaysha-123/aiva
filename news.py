import requests
import speak as sp

def news():
    main_url = "https://newsapi.org/v2/everything?q=tesla&from=2021-11-05&sortBy=publishedAt&apiKey=425675b8ff12423487e9e81200646ea4"
    main_page = requests.get(main_url).json()
    articles = main_page["article"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        sp.speak(f"Today's {day[i]} news is: {head[i]}")


