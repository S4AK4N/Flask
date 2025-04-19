from flask import Blueprint, render_template, request
from components.models.model import Name
from components.models.db import db

delete_routes = Blueprint("delete_action_routes", __name__)

# ===============================
# NOTE: 名前削除処理（POST）
# ===============================
@delete_routes.route("/delete_name", methods=["POST"])
def delete_name():
    try:
        name_to_delete = request.form.get("name")

        target = Name.query.filter_by(name=name_to_delete).first()

        if target:
            db.session.delete(target)
            db.session.commit()
            return render_template("success_delete_name.html", name=name_to_delete)
        else:
            return render_template("cant_delete_name.html", name=name_to_delete)


    except Exception as e:
        print(f"{e}を検知")
        Error_message = "名前削除中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)