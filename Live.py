from pip._vendor.distlib.compat import raw_input

import MemoryGame
import GuessGame
import CurrencyRouletteGame
import  Score
import Utils
def welcome(Name):
    print (f"Hello {Name} and welcome to the World of Games (WoG).Here you can find many cool games to play.")
    Score.CheckScoreFile()

def load_game():
    Game = raw_input("Please choose a game to play:"
                         "1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back"
                         "2. Guess Game - guess a number and see if you chose like the computer"
                         "3. Currency Roulette - try and guess the value of a random amount of USD in ILS, 4 to exit "

                            )
    if Game != '':
        GameNumber = int(Game)
        if GameNumber >= 1 and GameNumber <=4:
            Difficulty = int(raw_input("Please choose game difficulty from 1 to 5:"))
            if Difficulty >=1 and Difficulty <= 5:
                if GameNumber == 1:
                    Answer = MemoryGame.play(Difficulty)
                    if Answer:
                        Score.add_score(Difficulty)
                        Utils.Screen_cleaner()
                        load_game()
                    else:
                        Utils.Screen_cleaner()
                        load_game()
                if GameNumber == 2:
                    Answer = GuessGame.play(Difficulty)
                    if Answer:
                        print("You Right")
                        Score.add_score(Difficulty)
                        Utils.Screen_cleaner()
                        load_game()
                    else:
                        print("You not Right")
                        Utils.Screen_cleaner()
                        load_game()

            else:
                print("you choose worng number for difficulty choose right one")
                load_game()
        else:
            print("you choose wrong number Please Choose right one")
            load_game()
    else:
        print("print Any Number")
        load_game()





