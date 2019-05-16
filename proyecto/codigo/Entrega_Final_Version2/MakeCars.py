import os

class MakeCars:

    def __init__(self, cars):

        fileCars = open("Cars.txt", "w")
        
        for weight_path in cars:

            fileCars.write(str(weight_path[1]) + os.linesep)
