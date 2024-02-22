import asyncio
import httpx
import aiohttp
import asyncio
import aiofiles
from bs4 import BeautifulSoup
import re
from pathlib import Path
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


async def fetch_and_save_card_image(cardID):
    # 画像を取得するURL（ダミーで置き換える必要があります）

    async with httpx.AsyncClient() as client:
        response = await scrapefromcardID(cardID)

        # 画像データをファイルに保存
        filename = f"{cardID}.jpg"
        async with aiofiles.open(filename, "wb") as file:
            await file.write(response)

        return filename


async def create_pdf_and_cleanup(cardIDs, c, card_status):
    # 各カードIDに対して非同期に画像を取得し、ファイルに保存
    filenames = await asyncio.gather(
        *(fetch_and_save_card_image(cardID) for cardID in cardIDs)
    )
    print(filenames)

    # ここでPDFを作成する処理を実装
    # PDF作成ロジック（略）
    card_index = 0
    for k, v in card_status.items():
        for i in range(v):
            print(card_index)
            row = card_index % cards_per_column
            column = (card_index // cards_per_column) % cards_per_row

            # 新しいページの開始
            if card_index % (cards_per_row * cards_per_column) == 0 and card_index != 0:
                c.showPage()

            # カードの位置を計算
            x = margin_x + column * card_width
            y = page_height - margin_y - card_height - (row * card_height)

            # カード画像のファイル名
            card_image_filename = k + ".jpg"

            # カード画像をPDFに配置
            c.drawImage(card_image_filename, x, y, width=card_width, height=card_height)

            card_index += 1

    c.save()

    # PDF作成後、すべての画像ファイルを削除
    for filename in filenames:
        Path(filename).unlink()


async def scrapefromcardID(cardID):
    async with aiohttp.ClientSession() as session:
        url = f"https://www.pokemon-card.com/card-search/details.php/card/{cardID}/"
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            src = str(re.findall('src="(.*)"', str(soup.select("[class='fit']")))[0])
            image_url = f"https://www.pokemon-card.com{src}"
            async with session.get(image_url) as image_response:
                image = await image_response.read()
                return image


if __name__ == "__main__":
    card_status = {"44268": 2, "45209": 5, "41333": 4}  # 実際のカードIDに置き換える
    c = canvas.Canvas("test.pdf", pagesize=A4)
    cardIDs = ["41333", "44268", "45209"]  # 実際のカードIDに置き換える

    asyncio.run(create_pdf_and_cleanup(cardIDs, c, card_status))
