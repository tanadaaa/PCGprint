# これはなに

ポケカのデッキコードからプロキシ印刷用 PDF を生成できます
スクレイピングを使用しているのでほどほどに

# (windows) 実行方法

1. Docker Desktop をインストール [windows](https://docs.docker.com/desktop/install/windows-install/) [mac](https://docs.docker.com/desktop/install/mac-install/) [Linux](https://docs.docker.com/desktop/install/linux-install/)
2. Docker Desktop を起動
3. この右上の<>code から Download ZIP でローカルに落とし解凍し、Dockerfile があるディレクトリでターミナルを起動
4. `docker-compose up -d` でコンテナを起動
5. `http://localhost:5001/`にアクセス
6. デッキコードを入力し、生成ボタンを押すと 20 秒ほどしてダウンロードできるようになります
