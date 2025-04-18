# Pythonイメージ
FROM python:3.13.3-slim

# 作業ディレクトリ
WORKDIR /FLASK

# 依存関係
COPY  requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# アプリケーションのコードをコンテナにコピー
COPY . .

# Flaskアプリ起動
CMD ["python","app.py"]