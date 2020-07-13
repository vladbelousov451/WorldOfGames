# import only system from os
from os import system, name
import os

ScoreFile = "./Scores.text"
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "404"


def Screen_cleaner():
    os.system('clear')
