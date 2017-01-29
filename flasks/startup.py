from flask import Flask, render_template, request, jsonify
import json
import sys
import os
cwd = os.getcwd()
cwd = cwd[:-6]
cwd += 'web/'

sys.path.append(cwd)
import chess as game
import time


app = Flask(__name__)
parsedboard = {}
chessgame = game.rungame()
chessboard = game.Board()



@app.route('/', methods=['GET', 'POST'])
def initialize():
    return render_template('chess.html')

@app.route('/send/', methods=['POST'])
def sendDict():
    s1, s2, d1, d2 = [int(x) for x in raw_input("input: ").split()]
    chessboard.Move((s1, s2), (d1, d2), chessgame)
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
<<<<<<< HEAD
    jsondump = json.dumps(parsedboard)
<<<<<<< HEAD
return render_template('chess.html', title='Alexa Chess', testboard=jsondump)

@app.route('/restart/')
def restart():
    game.reset()
    start()
=======
    return render_template('chess.html', title='Alexa Chess', testboard=jsondump)



@app.route('/')
def initialize():
    chessboard = game.Board()
    return update()

@app.route('/waitformove/')
def waitformove():
    return update()
    #source, dest = alexa.Input().split()

@app.route('/checkmove/')
def checkmove():
    # chessboard.move(x1, y1, x2, y2, chessgame)
    return "ended"
    if chessboard.win():
        return "someone won"
    else:
        return redirect(url_for('waitformove'))

@app.route('/gameover/')
def restart():
    return 'ok' #new template
>>>>>>> ce0363a877ce21cf9624bb977c15510a77220ae9
=======
    return parsedboard
    # jsondump = json.dumps(parsedboard)
    # return render_template('chess.html', title='Alexa Chess', testboard=jsondump)
>>>>>>> de6e0b35afd577580f7a50c2342ceeb8d5a7e98b
