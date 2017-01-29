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
            if gameboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9812;'
            else:
                parsedboard[str(key)] = '&#9818;'
            continue
        if gameboard.board[key].piecetype == 'queen':
            if gameboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9813;'
            else:
                parsedboard[str(key)] = '&#9819;'
            continue
        if gameboard.board[key].piecetype == 'bishop':
            if gameboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9815;'
            else:
                parsedboard[str(key)] = '&#9821;'
            continue
        if gameboard.board[key].piecetype == 'knight':
            if gameboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9816;'
            else:
                parsedboard[str(key)] = '&#9822;'
            continue
        if gameboard.board[key].piecetype == 'rook':
            if gameboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9814;'
            else:
                parsedboard[str(key)] = '&#9820;'
            continue
    jsond = json.dumps(parsedboard)
    return render_template('chess.html', title='Alexa Chess', testboard=jsond)
