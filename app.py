from flask import Flask
from components.models.db import db
from components.views.router import views  # Blueprintルート登録
from components.models import model

# Flaskの設定
app = Flask(__name__)
app.register_blueprint(views)


# DB設定
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"  # SQLiteファイル名
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# DB初期化
db.init_app(app)

with app.app_context():
    db.create_all()
    print("✅ DBテーブル作成完了")

# アプリ起動
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)