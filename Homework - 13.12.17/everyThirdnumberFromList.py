#4) Write a Python function to print every third number from a list of numbers until the list becomes empty.


temperatureThisWeek  = [1, 2, 4, 1, 1, 3, 2,]

def third(temperatureThisWeek):
    res=[]
    count=3
    res.append(temperatureThisWeek[0])
    while len(temperatureThisWeek)>0:

        if count>0:
            temperatureThisWeek.pop(0)
        else:
            res.append(temperatureThisWeek[0])
            temperatureThisWeek.pop(0)
            count=3
        count -= 1
    return res

print (third(temperatureThisWeek))
