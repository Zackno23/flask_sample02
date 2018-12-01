import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("omikuji.html")


@app.route("/omikuji")
def hello():
    omikuji_list = ["大吉", '吉', '凶']
    return random.choice(omikuji_list)


if __name__ == '__main__':
    app.run(debug=True)

