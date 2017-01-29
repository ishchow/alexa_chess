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

def get_prompt():
    print("In get_prompt()")
    if "curr_player" not in session.attributes:
        session.attributes["curr_player"] = 0
    print(session.attributes["curr_player"])
    player_prompt = "Player {}, what is your move".format(session.attributes["curr_player"] + 1)
    session.attributes["curr_player"] = (session.attributes["curr_player"] + 1) % 1
    print(session.attributes["curr_player"])

    return player_prompt

# www.website.com/
@app.route('/')
def homepage():
    return "LET'S WIN HACKED 2017!!!!!"

@ask.launch
def launch():
    print("We've launched chess!")
    move_prompt = get_prompt()
    return question(move_prompt).reprompt(move_prompt)

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
    Source = unidecode(Source)
    Destination = unidecode(Destination)
    move_confirmation = "{} to {}".format(Source, Destination)
    move_prompt = get_prompt()
    speech_output = move_confirmation + move_prompt
    return question(speech_output).reprompt(move_prompt)

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
