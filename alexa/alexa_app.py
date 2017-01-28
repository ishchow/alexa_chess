from flask import Flask
from flask_ask import Ask, request, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/")

# www.website.com/
@app.route('/')
def homepage():
    return "LET'S WIN HACKED 2017!!!!!"

@ask.launch
def launch():
    welcome_message = 'Would you like to play chess?'
    return question(welcome_message)

@ask.intent("LaunchIntent_Yes")
def launched():
    msg = "Okay starting soon...."
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
    return "", 200

if __name__ == "__main__":
    app.run(debug=True)
