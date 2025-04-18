from flask import Blueprint, render_template, request

register_routes = Blueprint("register_name_routes", __name__)

# ===============================
# NOTE: 名前登録処理（POST）
# ===============================
@register_routes.route("/registration", methods=["POST"])
def registration():
    try:
        names = request.form.get("names")
        with open("names.txt", "a", encoding="utf-8") as file:
            file.write(names + "\n")
        return render_template("name_result.html", names=names)
    except Exception as e:
        return render_template("Error.html", Error="名前の登録中にエラーが発生しました")