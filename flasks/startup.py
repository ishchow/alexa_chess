from flask import Flask
from flask import render_template
import json
import classdef as game



app = Flask(__name__)


@app.route('/')
def start():
    parsedboard = {}
    gameboard = game.Board()
    for key in gameboard.board:
        if gameboard.board[key] == None:
            parsedboard[str(key)] = ' '
            continue
        if gameboard.board[key].piecetype == 'pawn':
            if gameboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9817;'
            else:
                parsedboard[str(key)] = '&#9823;'
            continue
        if gameboard.board[key].piecetype == 'king':
            parsedboard[str(key)] = 'k'
            continue
        if gameboard.board[key].piecetype == 'queen':
            parsedboard[str(key)] = 'q'
            continue
        if gameboard.board[key].piecetype == 'bishop':
            parsedboard[str(key)] = 'b'
            continue
        if gameboard.board[key].piecetype == 'knight':
            parsedboard[str(key)] = 'n'
            continue
        if gameboard.board[key].piecetype == 'rook':
            parsedboard[str(key)] = 'r'
            continue
    jsond = json.dumps(parsedboard)
    return render_template('chess.html', title='Alexa Chess', testboard=jsond)
