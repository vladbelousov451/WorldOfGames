from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
import Utils

scoreFile = Utils.ScoreFile

app = Flask(__name__)



import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)




@app.route('/')
def score_server():
    with open(scoreFile, "r") as File:
        Score = File.read()
        File.close()
    return render_template("index.html" , Scoreingame=Score )


def score_serve():

    app.run(host='0.0.0.0' )
