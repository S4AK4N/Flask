from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():

    savas  = "さばす"

    return render_template("index.html",savas = savas)

@app.route("/about")
def about():
    nemui = "ねむい"
    return render_template("another.html",nemui = nemui)

#TODO:チャプター5を進める(HTMLに変数受け渡し)