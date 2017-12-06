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
averageTemperatureList = [3, 4, 6, 9, 14, 17, 18, 17, 14, 11, 7, 4]
numberOfRainyDays = [22, 19, 19, 18, 17, 18, 19, 19, 20, 21, 21, 20]

def sandrapulse():
    for i in range(0, len(averageTemperatureList)):
        myTurtle.left(90)
        myTurtle.forward(averageTemperatureList[i])
        myTurtle.right(90)
        myTurtle.forward(25)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i])
        myTurtle.left(90)
        myTurtle.forward(20)





def pulse(height,width):
    myTurtle.left(90)
    myTurtle.forward(height*10)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height*10)
    myTurtle.left(90)
    myTurtle.forward(20)

for temp in averageTemperatureList:
    pulse(temp,25)

myTurtle = setupTurtle()

for temp in numberOfRainyDays:
    pulse(temp,25)

turtle.done()
