# Flask,Docker練習用リポジトリ

## 使用技術
<p>フロントエンド:HTML(jinja2),CSS</p>
<p>バックエンド:Python(Flask)</p>
<p>開発環境:Docker</p>

## バージョン等
| 言語・フレームワーク  | バージョン |
| --------------------- | ------------|
| Python                | 3.12.3      |
| Flask                 | 3.0.3       |
| Werkzeug              | 3.0.0       |
| Jinja2                | 3.1.0 ,3.2.0|
| itsdangerous          |2.1.2 ,2.2.0 |
| click                 | 8.0.0, 9.0.0|
<p>Flaskの依存環境も記述<p>

## ディレクトリ構成(現状)
```
.
├── Dockerfile # Docker環境
├── README.md 
├── __pycache__
│   └── app.cpython-312.pyc
├── app.py # サーバー処理記述
├── docker-compose.yml
├── names.txt　# 入力された名前記述(データーベース代わり)
├── requirements.txt # 本環境の必要ライブラリ等
├── static # 静的ファイル置き場
│   └── css
│       ├── form.css 
│       └── styles.css
├── templates # 各ページ置き場
│   ├── Error.html # エラー発生時遷移するページ
│   ├── cant_delete_name.html # 削除したい名前がなかった時表示するページ
│   ├── delete_name_form.html # 名前削除フォーム
│   ├── form.html # 内容投稿フォーム               
│   ├── form_past.html # 過去に投稿した内容を表示するフォーム
│   ├── form_result.html   # 内容投稿をした際に投稿内容を表示するページ
│   ├── index.html # トップページ
│   ├── layout.html # テンプレート
│   ├── name_registration.html # 名前登録フォーム
│   ├── name_result.html    # 登録(送信)した名前を表示するページ
│   └── success_delete_name.html # 正常に名前が削除できた際に表示するページ
└── text.txt
```
## 環境構築方法
Docker Desktop,Gitがインストールをお願いします。インストール方法は割愛致します。
<br>
<br>まず 上記のディレクトリ構成のうちの<strong>"myapp"</strong>に移動してください
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
<br>また今回はローカルサーバのみを想定しています。
<br>本番環境にする際はそれらに適した設定でお願いします。

### 注意点
<br> 今作では技量的にデータベースを連携することができなかったので投稿,名前登録などに関するセキュリティ面,利便性がかなり低くなっています。
<br>そのため,<strong>本番環境では使用しないでください</strong>あくまで練習用です。

## 課題,問題点,機能紹介について
<!--qiitaの記事を書け次第リンク追加-->
<br> qiitaにて記事を書いてますので、ぜひ<a href=https://qiita.com/nanashi39/private/03132761b850291d60f1>**こちら**</a>で御覧ください
