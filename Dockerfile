# Pythonランタイムを親イメージとして使用
FROM python:3.12.3

# 作業ディレクトリを/appに設定
WORKDIR /app

# 現在のディレクトリの内容をコンテナ内の/appにコピー
COPY . /app

# requirements.txtで指定された必要なパッケージをインストール
RUN pip install -r requirements.txt

# ポートの公開
EXPOSE 5000

# コンテナ起動時にFlaskアプリケーションを実行
CMD ["flask", "run", "--host=0.0.0.0"]
