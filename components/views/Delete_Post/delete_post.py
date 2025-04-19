from flask import Blueprint, render_template, request,redirect
from components.models.model import Post
from components.models.db import db

delete_post_routes = Blueprint("delete_post_routes", __name__)

@delete_post_routes.route("/delete_post/<int:id>", methods=["POST"])
def delete_post(id):
    try:
        post = Post.query.get(id)
        print("🧪 取得した投稿:", post)

        if post:
            db.session.delete(post)
            db.session.commit()
            return redirect("/past")
        else:
            print("⚠️ 投稿が見つからない")

        return render_template("success_delete_post.html", post=post)
    except Exception as e:
        print(f"{e} を検知")
        return render_template("Error.html", Error="投稿削除処理でエラーが発生しました")