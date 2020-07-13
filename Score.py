import Utils

ScoreFile = Utils.ScoreFile


def add_score(Diffuculty , ScoreFile=ScoreFile):
    with open(ScoreFile , "r") as ReadFile:
        Number = ReadFile.read()
        print(type(Number))
        TemplatePoints = (Diffuculty * 3) + 5
        Number2 = int(int(Number) + TemplatePoints)
        Number3 = str(Number2)
        with open(ScoreFile , 'w') as WriteFile:
            WriteFile.writelines(Number3)
            WriteFile.close()
    ReadFile.close()


        #if ReadFile.readline  0:
         #   Number = int(ReadFile.readline())
          #  with open(ScoreFile, "w+") as myfile:
           #     Number2 = int(Number + ((Diffuculty*3) +5 ) )
            #    Number3 = str(Number2)
             #   myfile.write(Number3 )
              #  myfile.close()
        #else:
         #   ReadFile.writeline(0)
          #  add_score(Diffuculty , ScoreFile=ScoreFile)
        #2
        # ReadFile.close()


def CheckScoreFile( ScoreFile=ScoreFile):
    with open(ScoreFile , "w+") as ReadFile:
        num_in_file = ReadFile.readline()
        if num_in_file == '':
            ReadFile.write("0")
            pass
    ReadFile.close()


