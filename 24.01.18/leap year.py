

def isLeapYear(year):
    if (year % 4) == 0 and not (year % 100) ==  0 and (year % 400) == 0:
        return "it's a leap year"
    else:
        return "not a leap year"


print(isLeapYear(2000))

