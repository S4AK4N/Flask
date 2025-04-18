from flask import Blueprint, render_template, request

post_routes = Blueprint("result_routes", __name__)
# ===============================
# NOTE: 名前,投稿内容を取得し投稿して書き込み確認ページに遷移,ファイルに書き込み
# ===============================
@post_routes.route("/result", methods=["GET", "POST"])
def result():
    try:
        if request.method == "POST":
            name = request.form["name"]
            article = request.form["article"]
        else:
            name = request.args.get("name")
            article = request.args.get("article")

        # ファイル追加書き込み(投稿内容をテキストファイルへ)
        with open("text.txt", "a", encoding="utf-8") as file:
            file.write(article + "," + name + "\n")

        return render_template("form_result.html", name=name, article=article)

    except Exception as e:
        print(f"{e}を検知")
        Error_message = "投稿処理中にエラー発生しました"
        return render_template("Error.html", Error=Error_message)