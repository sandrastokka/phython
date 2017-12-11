

temperatureThisWeek  = [1, 2, 3, 4, 5, 6, 7]

def addTemperatureThisWeek():
    sumOfList = 0
    print ("summing up the temprature of this week")
    for i in range(0, len(temperatureThisWeek)):
        sumOfList = sumOfList + temperatureThisWeek[i]
        print ("The sum of myList is", sumOfList)


addTemperatureThisWeek()
