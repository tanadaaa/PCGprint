import scrape
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import asyncio
import async_export_jpgs

# カードのサイズ (63mm x 88mm)
card_width = 64 * mm
card_height = 88 * mm

# A4用紙のサイズ
page_width, page_height = A4

# 1ページあたりのカードの配置数（3x3）
cards_per_row = 3
cards_per_column = 3

# 余白の計算 (ページの幅 - (カードの幅 * 一列あたりのカード数)) / 2
margin_x = (page_width - (card_width * cards_per_row)) / 2
margin_y = (page_height - (card_height * cards_per_column)) / 2


def export_pdf(deckcord, c):
    decks = scrape.scrapefromdeckcord(deckcord)
    if decks is None:
        return False
    card_status = {}
    cardIDs = []

    for card in decks:
        if card == "":
            continue
        status = card.split("_")
        cardID = status[0]
        cardnum = int(status[1])
        card_status[cardID] = cardnum
        cardIDs.append(cardID)

    async_export_jpgs.asyncio.run(
        async_export_jpgs.create_pdf_and_cleanup(cardIDs, c, card_status)
    )
    return True
