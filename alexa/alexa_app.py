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

curr_player = 0

# www.website.com/
@app.route('/')
def homepage():
    return "LET'S WIN HACKED 2017!!!!!"

@ask.launch
def launch():
    global curr_player
    player_prompt = "Player {}, what is your move".format(curr_player + 1)
    curr_player = (curr_player + 1) % 1
    print("We've launched chess!")
    return question(player_prompt).reprompt(player_prompt)

@ask.intent("GetFirstMove")
def get_first_move(Source, Destination):
    """ Gets first move from play

    Args:
        Source (unicode): from where player is moving chess piece
        Destination (unicode): to where player is moving chess piece

    Returns:
        Statement: Alexa repeats your move
    """
    print("First Move")
    Source = unidecode(Source)
    Destination = unidecode(Destination)
    msg = "{} to {}".format(Source, Destination)
    return statement(msg)

@ask.intent("GetNextMove")
def get_first_move(Source, Destination):
    print("First Move")
    Source = unidecode(Source)
    Destination = unidecode(Destination)
    msg = "{} to {}".format(Source, Destination)
    return statement(msg)

@ask.intent("LaunchIntent_No")
def fbomb_mlhstye():
    msg = "Your lame, cool people play chess!!!!"
    return statement(msg)

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")

@ask.session_ended
def session_ended():
    global curr_player
    curr_player = 0
    return "", 200

if __name__ == "__main__":
    app.run(debug=True)
