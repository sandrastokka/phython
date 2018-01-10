

#reading a file

def readMyDataFile(dataFileName):
    with open(dataFileName, mode='r')as myDataFile:
        print (type(myDataFile))
        items = myDataFile.read().splitlines()
        return items

#readMyDataFile()


def writeDataToMyFile(text):
    with open ("testing.txt",'w')as myDataFile:
        for item in text:
            myDataFile.write(item+'\n')

text = ['a' ,'b', 'c', 'd', 'e', 'f']
writeDataToMyFile(text)


def seeifItemExists(myItem):
    text = readMyDataFile('testing.txt')
    for item in text:
        if item == myItem:
            print (myItem, "Exist in my shopping list")
            return

    print (myItem, "Does not exist in my shopping list")



seeifItemExists("a")






