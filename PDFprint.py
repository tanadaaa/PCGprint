from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# PDFファイルの設定
output_filename = "cards.pdf"
c = canvas.Canvas(output_filename, pagesize=A4)

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


def create_pdf(img_src):
    # カード画像を配置
    for card_index in range(9):
        print(card_index)
        # 現在のページ内での行と列の位置を計算
        row = card_index % cards_per_column
        column = (card_index // cards_per_column) % cards_per_row

        # 新しいページの開始
        if card_index % (cards_per_row * cards_per_column) == 0 and card_index != 0:
            c.showPage()

        # カードの位置を計算
        x = margin_x + column * card_width
        y = page_height - margin_y - card_height - (row * card_height)

        # カード画像のファイル名
        card_image_filename = img_src

        # カード画像をPDFに配置
        c.drawImage(card_image_filename, x, y, width=card_width, height=card_height)

    # PDFファイルを保存
    c.save()


create_pdf("oriparu.jpg")
