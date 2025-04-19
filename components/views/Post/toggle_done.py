from flask import Blueprint, redirect
from components.models.model import Post
from components.models.db import db

toggle_done_routes = Blueprint("toggle_done_routes", __name__)
# ===============================
# NOTE: 完了、未完了の状態管理処理
# ===============================
@toggle_done_routes.route("/toggle_done/<int:id>", methods=["POST"])
def toggle_done(id):
    post = Post.query.get(id)
    if post:
        post.is_done = not post.is_done
        db.session.commit()
    return redirect("/past")