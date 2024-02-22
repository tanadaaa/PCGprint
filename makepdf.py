import scrape
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

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
    card_index = 0
    card_status = []

    for card in decks:
        if card == "":
            continue
        status = card.split("_")
        cardID = status[0]
        cardnum = int(status[1])
        card_status.append([cardID, cardnum])
        print(cardnum)
        print("カードID: " + cardID + " カード枚数: " + str(cardnum) + "\n")

    for card in card_status:
        cardID = card[0]
        cardnum = card[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            temp.write(scrape.scrapefromcardID(cardID))
            temp.seek(0)
            cardsrc = temp.name
            for i in range(int(cardnum)):
                print(card_index)
                row = card_index % cards_per_column
                column = (card_index // cards_per_column) % cards_per_row

                # 新しいページの開始
                if (
                    card_index % (cards_per_row * cards_per_column) == 0
                    and card_index != 0
                ):
                    c.showPage()

                # カードの位置を計算
                x = margin_x + column * card_width
                y = page_height - margin_y - card_height - (row * card_height)

                # カード画像のファイル名
                card_image_filename = cardsrc

                # カード画像をPDFに配置
                c.drawImage(
                    card_image_filename, x, y, width=card_width, height=card_height
                )

                card_index += 1

    c.save()
    return True
