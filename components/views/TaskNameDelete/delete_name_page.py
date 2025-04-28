from flask import Blueprint, render_template, request
from components.models.model import Name  # ← DBモデルをimport

delete_routes = Blueprint("delete_page_routes", __name__)

# ===============================
# NOTE: 削除フォームへのレンダリング
# ===============================
@delete_routes.route("/delete_name_form")
def delete_name_form():
    try:
        all_items = Name.query.all()
        return render_template("delete_name_form.html",all_items= all_items)
    except Exception as e:
        print(f"{e}を検知")
        Error_message = "削除フォームの表示中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)