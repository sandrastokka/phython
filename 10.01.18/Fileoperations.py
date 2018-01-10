

#reading a file

def readMyDataFile():
    with open("someDat.txt", mode='r')as myDataFile:
        print (type(myDataFile))
        clubs = myDataFile.read().splitlines()
        print(clubs)

readMyDataFile()


