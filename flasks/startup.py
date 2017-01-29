from flask import Flask
from flask import render_template
import json
import
#from game.Board import board as b


app = Flask(__name__)


@app.route('/')
def start():
    b = {}
    for i in range(8):
        for j in range(8):
            b["(1, 3)"] = j+i;
    jsond = json.dumps(b)
    return render_template('chess.html', title='Alexa Chess', testboard=jsond)
