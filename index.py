from flask import (
    Flask,
    request,
    send_from_directory,
    after_this_request,
    redirect,
    url_for,
    jsonify,
    render_template,
)
import os
import urllib.parse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import makepdf
import threading
import time

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # index.htmlを表示
    return render_template("form.html")


@app.route("/create-pdf", methods=["POST"])
def create_pdf_endpoint():
    # フォームからPDFファイル名を取得
    deckcord = request.form["deckcord"]
    # ファイル名に使用できない文字をエスケープまたは置換
    safe_pdf_name = urllib.parse.quote_plus(deckcord) + ".pdf"
    pdf_path = os.path.join("public", safe_pdf_name)

    c = canvas.Canvas(pdf_path, pagesize=A4)
    ok = makepdf.export_pdf(deckcord, c)
    if ok:
        # PDF作成成功時の処理

        # ファイル送信後にファイルを削除するためのクリーンアップ関数
        @after_this_request
        def remove_pdf(response):
            try:
                delayed_remove(pdf_path, 60)
            except Exception as error:
                app.logger.error(
                    "Error removing or closing downloaded file handle", error
                )
            return response

        # 作成したPDFファイルをユーザーに送信
        return send_from_directory("public", safe_pdf_name, as_attachment=True)
    else:
        # PDF作成失敗時の処理
        return jsonify({"error": "PDFの作成に失敗しました。"}), 500


def delayed_remove(path, delay):
    """指定された遅延後にファイルを削除する"""

    def remove_file():
        time.sleep(delay)
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error removing file: {e}")

    threading.Thread(target=remove_file).start()
