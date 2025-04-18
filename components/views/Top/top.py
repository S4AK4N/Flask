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