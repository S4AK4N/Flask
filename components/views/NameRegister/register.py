# components/views/NameRegister/register.py

from flask import Blueprint, render_template, request
register_routes = Blueprint("register_routes", __name__)

@register_routes.route("/name_registration")
def name_registration():
    try:
        return render_template("name_registration.html")
    except Exception as e:
        return render_template("Error.html", Error="名前登録のレダリング中にエラーが発生しました")

@register_routes.route("/registration", methods=["POST"])
def registration():
    try:
        names = request.form.get("names")
        with open("names.txt", "a", encoding="utf-8") as file:
            file.write(names + "\n")
        return render_template("name_result.html", names=names)
    except Exception as e:
        return render_template("Error.html", Error="名前の登録中にエラーが発生しました")