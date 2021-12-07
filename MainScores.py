from flask import Flask, render_template
from MainGame import *

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        scores_file = open("Scores.txt", "r")
        SCORE = int(scores_file.readline())
        return render_template('Score_server.html', SCORE=SCORE)
    except:
        return render_template('Score_server_error.html', ERROR=logging.ERROR)


if __name__ == '__main__':
    app.run()
