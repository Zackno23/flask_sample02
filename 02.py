import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/omikuji")
def hello():
    omikuji_list = ["大吉", '吉', '凶']
    result = random.choice(omikuji_list)
    return render_template("omikuji.html", result=result)






@app.route("/dice")
def dice_shuffle():
    dice_list = range(0, 5)
    return str(random.choice(dice_list))


if __name__ == '__main__':
    app.run(debug=True)
