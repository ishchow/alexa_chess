from flask import Flask, render_template, request, jsonify
import json
import sys
import os

cwd = os.getcwd()
cwd = cwd[:-6]
cwd += 'web/'
print cwd
sys.path.append(cwd)
import chess as game

cwd = cwd[:-4]
cwd += 'alexa/'
print cwd
sys.path.append(cwd)
import alexa_app



app = Flask(__name__)
parsedboard = {}
chessgame = game.rungame()
chessboard = game.Board()



@app.route('/', methods=['GET', 'POST'])
def initialize():
    return render_template('chess.html')

@app.route('/send/', methods=['POST'])
def sendDict():
    if request.is_json:
        j = request.get_json(force=True)
        s1, s2, d1, d2 = [int(x) for x in j[u'move'].split()]
        print(s1, s2, d1, d2)
        chessboard.Move((s1, s2-1), (d1, d2-1), chessgame)
    # s1, s2, d1, d2 = [int(x) for x in raw_input("imput: ").split()]
    # s1, s2, d1, d2 = 1, 1, 1, 2


    return jsonify(dict = update(chessboard))

def update(chessboard):
    parsedboard = {}
    for key in chessboard.board:
        if chessboard.board[key] == None:
            parsedboard[str(key)] = ' '
            continue
        if chessboard.board[key].piecetype == 'pawn':
            if chessboard.board[key].color == 'white':
                parsedboard[str(key)] = '&#9817;'
            else:
                parsedboard[str(key)] =  '&#9823;'
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
                parsedboard[str(key)] =  '&#9815;'
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
                parsedboard[str(key)] =  '&#9814;'
            else:
                parsedboard[str(key)] = '&#9820;'
            continue
    return parsedboard
    # jsondump = json.dumps(parsedboard)
    # return render_template('chess.html', title='Alexa Chess', testboard=jsondump)
