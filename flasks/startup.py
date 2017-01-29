from flask import Flask
from flask import render_template
import json
import web.chess as game



app = Flask(__name__)


@app.route('/')
def start():
    gameboard = game.Board()

    jsond = json.dumps(gameboard)
    return render_template('chess.html', title='Alexa Chess', testboard=jsond)
