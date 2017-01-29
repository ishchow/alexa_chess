from flask import Flask
from flask_ask import Ask, request, statement, question, session
import json
import requests
import time
from unidecode import unidecode
import logging

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

def change_player():
    if (session.attributes["curr_player"] == "White"):
        session.attributes["curr_player"] = "Black"
    else:
        session.attributes["curr_player"] = "White"
    print(session.attributes["curr_player"])

def get_prompt():
    print("In get_prompt()")
    print(session.attributes["curr_player"])
    player_prompt = "{} Player, what is your move?".format(session.attributes["curr_player"])

    return player_prompt

# www.website.com/
@app.route('/')
def homepage():
    return "LET'S WIN HACKED 2017!!!!!"

@ask.launch
def launch():
    print("We've launched chess!")
    session.attributes["curr_player"] = "White"
    session.attributes["board_id"] = {b_id:None for b_id in board_id}
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

    if (Source not in session.attributes["board_id"]) \
    or (Destination not in session.attributes["board_id"]):
    return question(get_prompt())
    print("Error! Try Again!")

    Source = unidecode(Source)
    Destination = unidecode(Destination)


    # Execute Current Player Move
    move_confirmation = "{} to {}".format(Source, Destination)
    card_title = "{} Player move".format(session.attributes["curr_player"])
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
    app.run(debug=True)
