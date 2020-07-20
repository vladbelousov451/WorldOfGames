from Live import load_game, welcome
import MainScores , threading
import Utils


print(welcome("Guy"))
Score_Thread = threading.Thread(target=MainScores.score_serve)
Game_Thread = threading.Thread(target=load_game)


Score_Thread.start()
Utils.Screen_cleaner()
Game_Thread.start()





