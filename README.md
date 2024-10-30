# Flask,Docker練習用リポジトリ

## 使用技術
<p>フロントエンド:HTML,CSS</p>
<p>バックエンド:Python(Flask),Mysql</p>
<p>開発環境:Docker</p>

## ディレクトリ構成(現状)
```
.
├── Dockerfile
├── README.md
├── __pycache__
│   └── app.cpython-312.pyc
├── app.py
├── docker-compose.yml
├── requirements.txt
└── templates
    ├── eat.html
    ├── index.html
    ├── layout.html
    └── walk.html
```
## 環境構築方法
Docker Desktop,Gitがインストール済みの前提でお話します。
<br>
<br>まず本リポジトリをクローンしてコンテナを作成します
<br>
<br>``` docker-compose build```
<br>
<br>次に作成したコンテナを起動します
<br>
<br>``` docker-compose up```
<br>
<br>うまく起動できたらローカルホストが立ち上がるのでそれで成功です。
<br>
<br>仕様等を変更したいときは再ビルドするようにしてください。
<br>
<br>また今回はローカルサーバのみを想定しています。5000ポートを使用してローカルに開放しています
<br><strong>コンテナ起動 = サーバ起動と考えていただいて結構です</strogn>