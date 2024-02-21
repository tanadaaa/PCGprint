from flask import Flask
from flask import render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/printed", methods=["GET", "POST"])
def sample_form():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        print("POSTデータ受け取ったので処理します。")
        req1 = request.form["deckcord"]
        return render_template("already.html", deckcord=req1)
