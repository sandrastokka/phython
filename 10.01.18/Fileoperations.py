

#reading a file

def readMyDataFile(dataFileName):
    with open(dataFileName, mode='r')as myDataFile:
        print (type(myDataFile))
        clubs = myDataFile.read().splitlines()
        return items

#readMyDataFile()


def writeDataToMyFile(text):
    with open ("testing.txt",'w')as myDataFile:
        for item in text:
            myDataFile.write(item+'\n')

text = ['a' ,'b', 'c', 'd', 'e', 'f']
writeDataToMyFile(text)

#somthing is wrong with the last part of the program, maybe the first as well

def seeifItemExists(myItem):
    myshoppinglist = readMyDataFile('testing.txt')
    for item in myshoppinglist:
        if item == myItem:
            print (myItem, "Exist n my shopping list")
            return

    print (myItem, "Does not exist in my shopping list")


    seeifItemExists("a")






