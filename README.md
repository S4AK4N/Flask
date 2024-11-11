# Flask,Docker練習用リポジトリ

## 使用技術
- **フロントエンド**: HTML (Jinja2), CSS
- **バックエンド**: Python (Flask)
- **開発環境**: Docker

## バージョン等

| 言語・フレームワーク  | バージョン     |
| --------------------- | -------------- |
| Python                | 3.12.3         |
| Flask                 | 3.0.3          |
| Werkzeug              | 3.0.0          |
| Jinja2                | 3.1.0, 3.2.0   |
| itsdangerous          | 2.1.2, 2.2.0   |
| click                 | 8.0.0, 9.0.0   |

Flaskの依存環境もこちらに記述しています。

## ディレクトリ構成

```
.
├── Dockerfile               # Docker環境
├── README.md                # このファイル
├── __pycache__              # コンパイル済みファイル
│   └── app.cpython-312.pyc
├── app.py                   # サーバー処理記述
├── docker-compose.yml       # コンテナ構成
├── names.txt               # 入力された名前を記述（データベース代わり）
├── requirements.txt         # 必要ライブラリ等
├── static                   # 静的ファイル置き場
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

Docker DesktopとGitがインストールされていることが前提です。インストール方法は割愛します。

まず、上記のディレクトリ構成のうち、`"myapp"` に移動してください。

### 1. リポジトリをクローンし、コンテナを作成

本リポジトリをクローンして、コンテナを作成します。

```bash
docker-compose build
```
うまく起動できたら、ローカルホストが立ち上がり、成功です。
### 3. 仕様変更後の再ビルド

仕様などを変更したい場合は、再ビルドを行ってください。

> **注意**: 今回はローカルサーバーのみを想定しています。本番環境にする際は、それらに適した設定を行ってください。

---

### 注意点
<br> 今作では技量的にデータベースを連携することができなかったので投稿,名前登録などに関するセキュリティ面,利便性がかなり低くなっています。
<br>そのため,<strong>本番環境では使用しないでください</strong>あくまで練習用です。

## 課題, 問題点, 機能紹介について

[Qiitaの記事をこちらで公開しています](https://qiita.com/nanashi39/private/03132761b850291d60f1)ので、ぜひご覧ください。


