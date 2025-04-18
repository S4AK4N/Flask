from flask import Blueprint, render_template, request

register_routes = Blueprint("register_name_page_routes", __name__)

# ===============================
# NOTE: 名前登録フォームレンダリング
# ===============================
@register_routes.route("/name_registration")
def name_registration():
    try:
        return render_template("name_registration.html")
    except Exception as e:
        return render_template("Error.html", Error="名前登録のレダリング中にエラーが発生しました")