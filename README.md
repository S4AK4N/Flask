# ToDoアプリ

## 使用技術

- **フロントエンド**: HTML (Jinja2), CSS
- **バックエンド**: Python (Flask)
- **開発環境**: Docker
- **デプロイ**: AWS(EC2)
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
├── README.md                
├── app.py                   # サーバー,DB起動処理
├── docker-compose.yml       # コンテナ構成
├── requirements.txt         # 必要ライブラリ等
├── instance/                # 永続化用ディレクトリ
│   ├──  app.db              # SQLiteデータベースファイル 
├── components/              # アプリケーション構成
│   ├── models               # モデル定義
│   └── views                # ビュー定義
├── static/                  # 静的ファイル置き場
│   └── css/
│       ├── form.css 
│       └── styles.css
└── templates/               # 各ページテンプレート
```

## 永続化について

アプリケーションはSQLiteを使用しており、データはinstance/の `app.db` に保存されます。Dockerコンテナの内部 `/FLASK/instance` を、ホスト側 `./instance` にマウントすることで永続化を実現しています。

## 環境構築方法

Docker DesktopとGitがインストールされていることが前提です。

```bash
docker-compose up --build
```

上記のみで、ビルド + 起動まで一括できます。

## デプロイについて
- セキュリティ面を考慮して、アクセスできるIPアドレスを制限を行なっております。
- [本アプリのリンク](https://todotask.zapto.org/)
- アクセスをしたい場合は以下のメールアドレスにアクセスをしたいという一言とIPアドレスを添えていただければと思います。
- kd1378732@st.kobedenshi.ac.jp


---

