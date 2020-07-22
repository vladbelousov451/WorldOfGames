# import only system from os
# Check Git webhook
from os import system, name


ScoreFile = "./Scores.text"
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "404"


def Screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
