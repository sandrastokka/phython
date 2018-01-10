

def readMyDataFile(dataFileName):
    with open(dataFileName, mode='r')as myDataFile:
        print (type(myDataFile))
        items = myDataFile.read().splitlines()
        return items

#readMyDataFile()




def checkPassword(userName):
    data = readMyDataFile("userCredentials.txt")
    print(data)
    for user in data:
        userCred = user.split(';')
        print (userCred)
        if (userCred[0] == userName):
            print ("Type password for", userName)
            userPass = input()
            if (userPass == userCred[1]):
                print ("The password is correct")

            else:
                print ("the Password for", userName, "is incorrect")



checkPassword("Dinesh")

#Still something wrong with the code





#seeifItemExists("a")
