from flask import Blueprint, render_template, request
from components.models.db import db
from components.models.model import Name

register_routes = Blueprint("register_name_routes", __name__)

# ===============================
# NOTE: 名前登録処理（POST）
# ===============================
@register_routes.route("/registration", methods=["POST"])
def registration():
    try:

        names = request.form.get("names")
        new_name = Name(name=names)
        db.session.add(new_name)
        db.session.commit()
        return render_template("name_result.html", names=names)
    except Exception as e:
        return render_template("Error.html", Error="名前の登録中にエラーが発生しました")