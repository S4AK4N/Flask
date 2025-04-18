# components/views/NameDelete/delete.py

from flask import Blueprint, render_template, request

delete_routes = Blueprint("delete_routes", __name__)

# NOTE:名前を削除するフォームに遷移処理
@delete_routes.route("/delete_name_form")
def delete_name_form():
    try:
        return render_template("delete_name_form.html")
    except Exception as e:
        print(f"{e}を検知")
        Error_message = "削除フォームの表示中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)

# NOTE:名前を削除する処理
@delete_routes.route("/delete_name", methods=["POST"])
def delete_name():
    try:
        names = request.form.get("name")

        # ファイルを読み込んでリスト化
        with open("names.txt", "r", encoding="utf-8") as file:
            file_content = file.readlines()

        # 名前がリストに含まれているか確認し、削除
        if names + "\n" in file_content:
            file_content.remove(names + "\n")

            # ファイルを上書きして変更を保存
            with open("names.txt", "w", encoding="utf-8") as file:
                file.writelines(file_content)

            return render_template("success_delete_name.html", name=names)
        else:
            return render_template("cant_delete_name.html", name=names)

    except Exception as e:
        print(f"{e}を検知")
        Error_message = "名前削除中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)