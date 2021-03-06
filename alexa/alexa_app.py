from flask import Flask
from flask_ask import Ask, request, statement, question, session
import json
import requests
import time
from unidecode import unidecode
import logging

class Move(object):
    def __init__(self):
        self.move = tuple()

m = Move()

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

board_id = [
    'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
    'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8',
    'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'
]

pa = [
    'alpha 1', 'alpha 2', 'alpha 3', 'alpha 4',
    'alpha 5', 'alpha 6', 'alpha 7', 'alpha 8', 'bravo 1',
    'bravo 2', 'bravo 3', 'bravo 4', 'bravo 5', 'bravo 6',
    'bravo 7', 'bravo 8', 'charlie 1', 'charlie 2', 'charlie 3',
    'charlie 4', 'charlie 5', 'charlie 6', 'charlie 7', 'charlie 8',
    'delta 1', 'delta 2', 'delta 3', 'delta 4', 'delta 5',
    'delta 6', 'delta 7', 'delta 8', 'echo 1', 'echo 2',
    'echo 3', 'echo 4', 'echo 5', 'echo 6', 'echo 7',
    'echo 8', 'foxtrot 1', 'foxtrot 2', 'foxtrot 3', 'foxtrot 4',
    'foxtrot 5', 'foxtrot 6', 'foxtrot 7', 'foxtrot 8', 'golf 1',
    'golf 2', 'golf 3', 'golf 4', 'golf 5', 'golf 6',
    'golf 7', 'golf 8', 'hotel 1', 'hotel 2', 'hotel 3',
    'hotel 4', 'hotel 5', 'hotel 6', 'hotel 7', 'hotel 8']

# def change_player():
#     if (session.attributes["curr_player"] == "White"):
#         session.attributes["curr_player"] = "Black"
#     else:
#         session.attributes["curr_player"] = "White"
#     print(session.attributes["curr_player"])

def get_prompt():
    print("In get_prompt()")
    player_prompt = "Player, what is your move?"

    return player_prompt

def parse(Source, Destination):
    print("In parse")
    if (Source in session.attributes["pa"]):
        pa_ch, num = Source.lower().split()
        s = pa_ch[0] + num
    else:
        s = Source.lower()

    if (Destination in session.attributes["pa"]):
        pa_ch, num = Destination.lower().split()
        d = pa_ch[0] + num
    else:
        d = Destination.lower()

    m.self = str(ord(s[0]) - ord('a')) + " " + str(ord(s[1]) - ord('0')) \
                + " " + str(ord(d[0]) - ord('a')) + " " + str(ord(d[1]) - ord('0'))
    print(m.self)
    d = {"move":m.self}
    res = requests.post("http://127.0.0.1:5000/send/", json=d)
    print res.text

# www.website.com/
@app.route('/alexa')
def homepage():
    return "LET'S WIN HACKED 2017!!!!!"

@ask.launch
def launch():
    print("We've launched chess!")
    session.attributes["board_id"] = {b_id:None for b_id in board_id}
    session.attributes["pa"] = {pa_ch:None for pa_ch in pa}
    launch_prompt = "Starting game..."
    move_prompt = get_prompt()
    speech_output = launch_prompt + move_prompt
    card_title = "Launched"
    return question(speech_output).reprompt(move_prompt).simple_card(card_title, "")

@ask.intent("MoveIntent")
def get_move(Source, Destination):
    """ Gets previous move from one player and asks for next move of second player

    Args:
        Source (unicode): from where player is moving chess piece
        Destination (unicode): to where player is moving chess piece

    Returns:
        Statement: Alexa repeats your move
    """
    print("Move Intent")

    # if Source is None or Destination is None:
    #     print("Error! Try Again!")
    #     return question(get_prompt())
    #
    # if (Source not in session.attributes["board_id"]) \
    # or (Source not in session.attributes["pa"]) \
    # or (Destination not in session.attributes["board_id"]) \
    # or (Destination not in session.attributes["pa"]):
    #     print("Error! Try Again!")
    #     return question(get_prompt())

    Source = unidecode(Source)
    Destination = unidecode(Destination)

    print(Source, ", ", Destination)
    parse(Source, Destination)

    # Execute Current Player Move
    move_confirmation = "{} to {}".format(Source, Destination)
    card_title = "Player move"
    card_out = move_confirmation

    # Get Next Player's Move
    change_player()
    move_prompt = get_prompt()
    speech_output = move_confirmation + move_prompt
    return question(speech_output).reprompt(move_prompt).simple_card(card_title, card_out)

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")

@ask.session_ended
def session_ended():
    return "", 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)
