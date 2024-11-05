from flask import Flask, render_template,request
import codecs
app = Flask(__name__)



savas = "さばす"

# NOTE:routeにアクセスした時,トップページに遷移
@app.route("/")
def top():

    return render_template("index.html",savas=savas)


# NOTE:/formにアクセスした時,フォームに遷移
@app.route("/form")
def show():
    
    file = codecs.open("names.txt","r","utf-8")
    all_names = [name.strip() for name in file.readlines()]
    file.close()

    return render_template("form.html",names = all_names)

# NOTE:/名前登録フォームへ遷移
@app.route("/name_registration")
def name_registration():

    return render_template("name_registration.html")


# NOTE:名前,投稿内容を取得し投稿して書き込み確認ページに遷移,ファイルに書き込み
@app.route("/result", methods=["GET", "POST"])
def result():

    # POSTメソッドの場合
    if request.method == "POST":
        name = request.form["name"]
        article = request.form["article"]
        # ファイル追加書き込み(投稿内容をテキストファイルへ)        
        file = codecs.open("text.txt","a","utf-8")         # ファイルオープン
        file.write(article + "," + name +"\n")              # 書き込み処理
        file.close()                                        # ファイルクローズ

    # GETメソッドの場合
    else:
        name = request.args.get("name")
        article = request.args.get("article")
        # ファイル追加書き込み(投稿内容をテキストファイルへ)        
        file = codecs.open("text.txt","a","utf-8")     # ファイルオープン
        file.write(article + "," + name +"\n")          # 書き込み処理
        file.close()                                    # ファイルクローズ

    return render_template("form_result.html", name=name, article=article)

# NOTE:過去投稿読み込んで表示
@app.route("/past")
def past():
    file = codecs.open("text.txt","r","utf-8")
    pasts = file.readlines()
    file.close()
    
    return render_template("form_past.html",pasts=pasts)

@app.route("/registration",methods = ["POST"])
def registration():
    names = request.form.get("names")
    file = codecs.open("names.txt","a","utf-8")
    file.write(names + "\n") # 改行しながら書き込み
    file.close()
    

    return render_template("name_result.html",names = names)
