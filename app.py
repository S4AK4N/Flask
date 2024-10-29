from flask import Flask, render_template,request
app = Flask(__name__)

savas  = "さばす"

#NOTE:
@app.route("/")
def top():

    return render_template("index.html",savas=savas)

#NOTE:routeにアクセスした時
@app.route("/form")
def show():

    return render_template("form.html",savas = savas)

#NOTE:form.htmlでtext,nameがsubmitで押された時,/resultを走らせるようにした
@app.route("/result",methods =["POST"])
def result():
    name = request.form["name"]
    text = request.form["text"]

    return render_template("form.html",savas=savas,name=name,text=text)
@app.route("/about")
def about():
    nemui = "ねむい"
    return render_template("another.html",nemui = nemui)


@app.route("/walk")
def walk():
    message = savas + "は歩いてるよ～"
    return render_template("walk.html",savas = savas , message = message)

#NOTE:/eatにアクセスした時,以下の内容を送信した,eat.htmlをブラウザに表示
@app.route("/eat")
def eat():
    foodlist = ["りんご","みかん","メロン"]
    return render_template("eat.html",savas=savas , foodlist = foodlist)


#TODO:チャプター5を進める(HTMLに変数受け渡し)