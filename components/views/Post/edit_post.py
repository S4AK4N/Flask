from flask import Blueprint, render_template, request, redirect
from components.models.model import Post
from components.models.db import db


edit_post_routes = Blueprint("edit_post_routes", __name__)

@edit_post_routes.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    try:
        post = Post.query.get(id)
        if not post:
            return render_template("Error.html", Error="該当の投稿が見つかりませんでした")
        
        # POSTメソッドの時のみ編集処理を行う
        if request.method == "POST":
            name = request.form.get("name")
            article = request.form.get("article")
            # バリテーション
            if not name or not article:
                return render_template("form_edit.html", post=post, error="未入力の項目があります")

            post.name = name
            post.article = article
            db.session.commit()

            return render_template("success_edit_post.html", post=post)
        return render_template("form_edit.html", post=post)

    except Exception as e:
        print(f"{e}を検知")
        return render_template("Error.html", Error="編集処理でエラーが発生しました")