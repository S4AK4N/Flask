from flask import Flask, render_template, request
import codecs

app = Flask(__name__)

# NOTE: routeにアクセスした時,トップページに遷移
@app.route("/")
def top():
    try:
        return render_template("index.html")

    except Exception as e:
        print(f"{e}を検知")
        Error_message = "トップページのレダリング中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)

# NOTE: /formにアクセスした時,フォームに遷移
@app.route("/form")
def show():
    try:
        file = codecs.open("names.txt", "r", "utf-8")
        all_names = [name.strip() for name in file.readlines()]
        file.close()
        return render_template("form.html", names=all_names)
    
    except Exception as e:
        print(f"{e}を検知")
        Error_message = "フォームを読み込む際にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)

# NOTE: /名前登録フォームへ遷移
@app.route("/name_registration")
def name_registration():
    try:
        return render_template("name_registration.html")
    
    except Exception as e:
        Error_message = "名前登録のレダリング中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)

# NOTE: 名前,投稿内容を取得し投稿して書き込み確認ページに遷移,ファイルに書き込み
@app.route("/result", methods=["GET", "POST"])
def result():
    try:
        # POSTメソッドの場合
        if request.method == "POST":
            name = request.form["name"]
            article = request.form["article"]
            try:
                # ファイル追加書き込み(投稿内容をテキストファイルへ)
                with codecs.open("text.txt", "a", "utf-8") as file:
                    file.write(article + "," + name + "\n")
            
            except Exception as e:
                print(f"{e}を検知")
                raise Exception("ファイル書き込み中にエラーが発生しました")

        # GETメソッドの場合
        else:
            name = request.args.get("name")
            article = request.args.get("article")
            try:
                # ファイル追加書き込み(投稿内容をテキストファイルへ)
                with codecs.open("text.txt", "a", "utf-8") as file:
                    file.write(article + "," + name + "\n")
            
            except Exception as e:
                print(f"{e}を検知")
                raise Exception("ファイル書き込み中にエラーが発生しました")

        return render_template("form_result.html", name=name, article=article)
    
    except Exception as e:
        print(f"{e}を検知")
        Error_message = "投稿処理中にエラー発生しました"
        return render_template("Error.html", Error=Error_message)

# NOTE: 過去投稿読み込んで表示
@app.route("/past")
def past():
    try:
        with codecs.open("text.txt", "r", "utf-8") as file:
            pasts = file.readlines()
        return render_template("form_past.html", pasts=pasts)
    
    except Exception as e:
        print(f"{e}を検知")
        Error_message = "過去の投稿読み込み中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)

# NOTE:名前を登録処理
@app.route("/registration", methods=["POST"])
def registration():
    try:
        names = request.form.get("names")
        with codecs.open("names.txt", "a", "utf-8") as file:
            file.write(names + "\n")  # 改行しながら書き込み
        return render_template("name_result.html", names=names)
    
    except Exception as e:
        print(f"{e}を検知")
        Error_message = "名前の登録中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)


# NOTE:名前を削除するフォームに遷移処理
@app.route("/delete_name_form")
def delete_name_form():
    try:
        return render_template("delete_name_form.html")
    
    except Exception as e:
        print(f"{e}を検知")
        Error_message = "削除フォームの表示中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)

# NOTE:名前を削除する処理
@app.route("/delete_name", methods=["POST"])
def delete_name():
    try:
        names = request.form.get("name")

        # ファイルを読み込んでリスト化
        with codecs.open("names.txt", "r", "utf-8") as file:
            file_content = file.readlines()

        # 名前がリストに含まれているか確認し、削除
        if names + "\n" in file_content:
            file_content.remove(names + "\n")

            # ファイルを上書きして変更を保存
            with codecs.open("names.txt", "w", "utf-8") as file:
                file.writelines(file_content)

            return render_template("success_delete_name.html", name=names)

        # その名前が登録されていなかった時
        else:
            return render_template("cant_delete_name.html", name=names)
    
    except Exception as e:
        print(f"{e}を検知")
        Error_message = "名前削除中にエラーが発生しました"
        return render_template("Error.html", Error=Error_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)
