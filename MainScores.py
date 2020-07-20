from flask import Flask
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
        if Score == '':
            ERROR = Utils.BAD_RETURN_CODE
            HTML = (f"""
            <html>
<head>
<title>Scores Game</title>
</head>
<body>
<body>
<h1><div id="score" style="color:red">{ERROR}</div></h1>
</body>
</html>
            
            """)
        else:
            HTML = (f""" <html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <h1>The score is <div id="score">{Score}</div></h1>
    </body>
    </html> """)
        return HTML

def score_serve():

    app.run(host='0.0.0.0' )
