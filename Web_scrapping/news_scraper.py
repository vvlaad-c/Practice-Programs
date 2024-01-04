import requests
from bs4 import BeautifulSoup

def get_news(url):
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.text, "html.parser")

    anchor_el = soup.find_all("h3")

    print("The main news articles:")
    if anchor_el:
        for anchor in anchor_el[:-3]:
            news_title = anchor.get_text()
            if len(news_title) > 1:
                print(news_title)
    else:
        print("Unable to fetch the news articles")
