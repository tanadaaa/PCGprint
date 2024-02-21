import requests
from bs4 import BeautifulSoup


def scrape(deckcord):
    url = f"https://www.pokemon-card.com/deck/result.html/deckID/{deckcord}/"
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup.prettify())


scrape("gngH9n-m4H2fV-gnHLgL")
