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
├── Dockerfile(コンテナ環境)
├── README.md
├── __pycache__
│   └── app.cpython-312.pyc
├── app.py→サーバーの処理(バックエンド)
├── docker-compose.yml（Docker起動用)
├── names.txt
├── requirements.txt(必要モジュールダウンロード用)
├── static　→静的ファイル
│   └── css
│       ├── form.css
│       └── styles.css
├── templates →　作成したページのHTMLたち
│   ├── form.html →　フォーム投稿ページ
│   ├── form_past.html →　過去投稿一覧表示ページ
│   ├── form_result.html　→ 投稿確認ページ
│   ├── index.html →　トップページ
│   ├── layout.html →　テンプレート
│   ├── name_registration.html →　名前登録をページ
│   └── name_result.html →　名前登録確認ページ
└── text.txt　→投稿等書き込み用
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

### 個人的な課題点など
<!--qiitaの記事を書け次第リンク追加-->
<br> qiitaにて記事を書いておりますので<a href=>こちら</a>で御覧ください
