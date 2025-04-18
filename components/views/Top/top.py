from flask import Blueprint, render_template
views = Blueprint("views", __name__)

# トップページ
@views.route("/")
def top():
    try:
        return render_template("index.html")
    except Exception as e:
        Error_message = "トップページのレダリング中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)

# フォームページ（名前一覧表示）
@views.route("/form")
def show():
    try:
        with open("names.txt", "r", encoding="utf-8") as file:
            all_names = [name.strip() for name in file.readlines()]
        return render_template("form.html", name=all_names)
    except Exception as e:
        Error_message = "フォームを読み込む際にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)