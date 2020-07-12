import Utils

ScoreFile = Utils.ScoreFile


def add_score(Diffuculty , ScoreFile=ScoreFile):
    with open(ScoreFile , "r") as ReadFile:
        Number = int(ReadFile.readline())
        with open(ScoreFile, "w+") as myfile:
            Number2 = int(Number + ((Diffuculty*3) +5 ) )
            Number3 = str(Number2)
            myfile.write(Number3 )
            myfile.close()
    ReadFile.close()






