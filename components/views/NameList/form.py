from flask import Blueprint, render_template

form_routes = Blueprint("form_routes", __name__)

# ===============================
# NOTE: 基本フォームへのレンダリング
# ===============================
@form_routes.route("/form")
def show():
    try:
        with open("names.txt", "r", encoding="utf-8") as file:
            all_names = [name.strip() for name in file.readlines()]
        return render_template("form.html", name=all_names)
    except Exception as e:
        Error_message = "フォームを読み込む際にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)