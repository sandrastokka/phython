import turtle

myTurtle = turtle.Turtle()
#mySecondTurtle = turtle.Turtle()

myList = [1, 2, 3, 5, 8, 21, 29, 50, 79, 129, 208, 337, 545]

print(myList)
print(myList[0])
print(myList[4])

#definingthefunction
def printMyList():
    print ("In the function")
    for i in range(0, len(myList)):
        print(myList[i])


#callingthefuncton
printMyList()


def addMyList():
    sumOfList = 0
    print ("summing up my list of numbers")
    for i in range(0, len(myList)):
        sumOfList = sumOfList + myList[i]
        print ("The sum of myList is", sumOfList)

addMyList()

def usingTurtleWithLists():
    for i in range(0, len(myList)):
        myTurtle.forward(myList[i])
        myTurtle.right(90)

usingTurtleWithLists()
turtle.done()


