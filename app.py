from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():

    hello = "hello"

    return render_template("index.html",hello = hello)

@app.route("/about")
def about():
    nemui = "ねむい"
    return render_template("another.html",nemui = nemui)

#TODO:チャプター5を進める(HTMLに変数受け渡し)