


import requests
import json
import random



response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")

json_data = json.loads(response.text)
from pip._vendor.distlib.compat import raw_input

ShekelCurrncy =json_data["rates"]['ILS']

rand_number = random.randint(1,100)



def get_money_interval(ShekelCurrncy , Difficulty):
    afterExchange = int(rand_number*ShekelCurrncy)
    guessFromUser = (afterExchange - (5 -Difficulty), afterExchange + (5-Difficulty))
    return guessFromUser


def get_guess_from_user():
    Guess = raw_input("guess Number")
    return Guess


def play(Difficulty):
    theNumber = get_money_interval(ShekelCurrncy , Difficulty )
    Guess = get_guess_from_user()
    if theNumber == Guess:
        return True
    else:
        return False








