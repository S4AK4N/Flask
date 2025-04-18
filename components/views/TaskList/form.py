from flask import Blueprint, render_template
from components.models.model import Name  # ← DBモデルをimport

form_routes = Blueprint("form_routes", __name__)

# ===============================
# NOTE: 基本フォームへのレンダリング
# ===============================
@form_routes.route("/form")
def show():
    try:
        # タスクを全権取得
        all_names = Name.query.all()

        # 取得したタスクをリストに格納(json用)
        # names = [n.name for n in all_names]
        
        return render_template("form.html", task_names=all_names)

    except Exception as e:
        Error_message = "フォームを読み込む際にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)