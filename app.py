from flask import Flask, render_template,request
app = Flask(__name__)

names = ["さばす","TanakaMasahiko","KawaiShinzoV2"]
savas = "さばす"
# NOTE:routeにアクセスした時
@app.route("/")
def top():

    return render_template("index.html",savas=savas)

# NOTE:routeにアクセスした時
@app.route("/form")
def show():


    return render_template("form.html",names = names)

# NOTE:form.htmlでtext,nameがsubmitで押された時,/resultを走らせるようにした
@app.route("/result", methods=["GET", "POST"])
def result():

    # POSTメソッドの場合
    if request.method == "POST":
        name = request.form["name"]
        text = request.form["article"]  # `text`ではなく`article`に変更
    # GETメソッドの場合
    else:
        name = request.args.get("name")
        text = request.args.get("text")

    return render_template("form_result.html", name=name, text=text)




#TODO:チャプター5を進める(HTMLに変数受け渡し)