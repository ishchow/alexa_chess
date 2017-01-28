from flask import Flask
from flask_ask import Ask, request, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

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
    return question(player_prompt).reprompt(player_prompt)

@ask.intent("GetFirstMove",
            mapping={'Source':'src', 'Destination':'dest'},
            convert={'src':'str', 'dest':'str'}
            )
def get_first_move(src, dest):
    print(type(src))
    print(src, dest)
    msg = "Move successful"
    statement(msg)

@ask.intent("GetNextMove",
            mapping={'Source':'src', 'Destination':'dest'})
def get_next_move(src, dest):
    print(src, dest)
    msg = "Move successful"
    statement(msg)

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
