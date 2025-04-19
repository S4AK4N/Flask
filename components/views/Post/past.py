from flask import Blueprint, render_template, request
from components.models.model import Post

past_routes = Blueprint("past_routes", __name__)

# ===============================
# NOTE: 過去投稿読み込んで表示
# ===============================
@past_routes.route("/past")
def past():
    try:
        # DBから全件取得
        pasts = Post.query.all()  
        return render_template("form_past.html", pasts=pasts)

    except Exception as e:
        print(f"{e}を検知")
        Error_message = "過去の投稿読み込み中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)
