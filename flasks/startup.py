from flask import Flask, render_template, request, redirect, url_for
import json
import sys
sys.path.append('/home/cmput274/kdehaan/Python/alexa_chess/web')
import chess as game


app = Flask(__name__)
parsedboard = {}
chessgame = game.rungame()
chessboard = game.Board()
def

def update():
    for key in chessboard.board:
        if chessboard.board[key] == None:
            parsedboard[str(key)] = ' '
            continue
        if chessboard.board[key].piecetype == 'pawn':
            if chessboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9817;'
            else:
                parsedboard[str(key)] = '&#9823;'
            continue
        if chessboard.board[key].piecetype == 'king':
            if chessboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9812;'
            else:
                parsedboard[str(key)] = '&#9818;'
            continue
        if chessboard.board[key].piecetype == 'queen':
            if chessboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9813;'
            else:
                parsedboard[str(key)] = '&#9819;'
            continue
        if chessboard.board[key].piecetype == 'bishop':
            if chessboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9815;'
            else:
                parsedboard[str(key)] = '&#9821;'
            continue
        if chessboard.board[key].piecetype == 'knight':
            if chessboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9816;'
            else:
                parsedboard[str(key)] = '&#9822;'
            continue
        if chessboard.board[key].piecetype == 'rook':
            if chessboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9814;'
            else:
                parsedboard[str(key)] = '&#9820;'
            continue
    jsondump = json.dumps(parsedboard)
    return render_template('chess.html', title='Alexa Chess', testboard=jsondump)



@app.route('/')
def initialize():
    chessboard = Board()
    update()

@app.route('/waiting/')
def waiting():
    source, dest = alexaInput().split()

@app.route('/checking/')
    move(x1, y1, x2, y2):
    update()
    def gotowait():
        return redirect(url_for('waiting'))
