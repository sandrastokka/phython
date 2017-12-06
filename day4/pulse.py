import turtle

def setupTurtle():
    myTurtleInsideTheFunction = turtle.Turtle()
    myTurtleInsideTheFunction.penup()
    myTurtleInsideTheFunction.setpos(-300,0)
    myTurtleInsideTheFunction.pendown()
    myTurtleInsideTheFunction.color('green')
    myTurtleInsideTheFunction.pensize(3)

    return myTurtleInsideTheFunction


#call the setupTurtle function and store the result in a variable
#called myTurtle
myTurtle = setupTurtle()

#define the temperature list
averageTemperatureList = [3, 4, 6, 9, 14, 17, 18, 200, 17, 14, 11, 7, 4]

def pulse():
    for i in range(0, len(averageTemperatureList)):
        myTurtle.left(90)
        myTurtle.forward(averageTemperatureList[i])
        myTurtle.right(90)
        myTurtle.forward(25)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i])
        myTurtle.left(90)
        myTurtle.forward(20)

pulse()
turtle.done()
