
def maxInList(myList):

    maxNumber = -1000

    for i in range (0, len(myList)):
        if maxNumber < myList[i]:
            maxNumber = myList [i]
            print ("Maxnumber now is :", maxNumber)

    return maxNumber



print (maxInList([1 , 3, 5, 0, -1, 21, 15, 7, 200, -9]))

