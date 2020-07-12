import Utils

scoreFile = Utils.ScoreFile

from flask import Flask
app = Flask(__name__)



@app.route('/')
def score_server():
    with open(scoreFile , "r") as File:
        Score = File.read()
        HTML = (f"<html>" \
               "<head>" \
               "<title>Scores Game</title>" \
               "</head>" \
               "<body>" \
               "<h1>The score is <div id=Score> {} </div></h1>" \
                                               "</body>" \
                                               "</html>").format(Score)
        return  HTML



if __name__ == '__main__':
    app.run()
