from flask import Flask
import Utils

scoreFile = Utils.ScoreFile

app = Flask(__name__)


@app.route('/')
def score_server():
    with open(scoreFile, "r") as File:
        Score = File.read()
        HTML = (f""" <html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{Score}</div></h1>
</body>
</html> """)
        return HTML

app.run()



app.run()