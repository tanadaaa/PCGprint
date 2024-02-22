# これはなに

ポケカのデッキコードからプロキシ印刷用PDFを生成できます

# (windows) 実行方法

右上の<>codeからDownload ZIPでローカルに落とし解凍し、index.pyがあるディレクトリでターミナルを起動して行ってください
1. [Python](https://www.python.org)をインストール
2. `python -m pip install -r requirements.txt`で必要なライブラリをインストール
3. `flask --app index --debug run`で実行
4. `http://127.0.0.1:5000`にアクセス
5. デッキコードを入力して提出した後、15 秒程度待つと PDF がダウンロードのアラートが出ます
