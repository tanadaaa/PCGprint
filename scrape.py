import requests
from bs4 import BeautifulSoup
import re


def scrapefromdeckcord(deckcord):
    url = f"https://www.pokemon-card.com/deck/result.html/deckID/{deckcord}/"
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text, "html.parser")
    errortext = str(
        re.findall(
            '<h1 class="Heading1">(.*)</h1>', str(soup.select("[class='Heading1']"))
        )[0]
    )
    print(errortext)
    if errortext == "デッキコードエラー":
        print("デッキコードエラーです。")
        return None
    else:
        print("デッキコードは正常です。")
    deckcards = soup.select("[id='inputArea']")
    deck_pke = re.findall(
        '<input id="deck_pke" name="deck_pke" type="hidden" value="(.*)">',
        str(deckcards),
    )[0].split("-")
    deck_gds = re.findall(
        '<input id="deck_gds" name="deck_gds" type="hidden" value="(.*)">',
        str(deckcards),
    )[0].split("-")
    deck_tool = re.findall(
        '<input id="deck_tool" name="deck_tool" type="hidden" value="(.*)">',
        str(deckcards),
    )[0].split("-")
    deck_tech = re.findall(
        '<input id="deck_tech" name="deck_tech" type="hidden" value="(.*)">',
        str(deckcards),
    )[0].split("-")
    deck_sup = re.findall(
        '<input id="deck_sup" name="deck_sup" type="hidden" value="(.*)">',
        str(deckcards),
    )[0].split("-")
    deck_sta = re.findall(
        '<input id="deck_sta" name="deck_sta" type="hidden" value="(.*)">',
        str(deckcards),
    )[0].split("-")
    deck_ene = re.findall(
        '<input id="deck_ene" name="deck_ene" type="hidden" value="(.*)">',
        str(deckcards),
    )[0].split("-")
    deck_ajs = re.findall(
        '<input id="deck_ajs" name="deck_ajs" type="hidden" value="(.*)">',
        str(deckcards),
    )[0].split("-")

    decks = (
        deck_pke
        + deck_gds
        + deck_tool
        + deck_tech
        + deck_sup
        + deck_sta
        + deck_ene
        + deck_ajs
    )

    return decks


def errorscrape(deckcord):
    url = f"https://www.pokemon-card.com/deck/result.html/deckID/{deckcord}/"
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text, "html.parser")
    errortext = str(
        re.findall(
            '<h1 class="Heading1">(.*)</h1>', str(soup.select("[class='Heading1']"))
        )[0]
    )
    print(errortext)
    if errortext == "デッキコードエラー":
        print("デッキコードエラーです。")


def scrapefromcardID(cardID):
    url = f"https://www.pokemon-card.com/card-search/details.php/card/{cardID}/"
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text, "html.parser")
    src = str(re.findall('src="(.*)"', str(soup.select("[class='fit']")))[0])
    response = requests.get(f"https://www.pokemon-card.com{src}")
    image = response.content
    return image


# scrapefromdeckcord("gngH9n-m4H2fV-gnHLgL")
# errorscrape("gngH9n-m4H2fV-gnHgha")
# scrapefromcardID("42288")
