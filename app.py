from flask import Flask, render_template,request
app = Flask(__name__)

savas  = "さばす"

# NOTE:routeにアクセスした時
@app.route("/")
def top():

    return render_template("index.html",savas=savas)

# NOTE:routeにアクセスした時
@app.route("/form")
def show():

    return render_template("form.html",savas = savas)

# NOTE:form.htmlでtext,nameがsubmitで押された時,/resultを走らせるようにした
@app.route("/result",methods =["GET","POST"])
def result():
    
    # POSTメソッドが戻り値だった時 
    if request.method == "POST":

        name = request.form["name"]
        text = request.form["text"]
    #GETメソッドだった時
    else:
        name = request.args.get("name")
        text = request.args.get("text")
    return render_template("form.html",savas=savas,name=name,text=text)


@app.route("/about")
def about():
    nemui = "ねむい"
    return render_template("another.html",nemui = nemui)

# NOTE:walkにアクセスした時
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