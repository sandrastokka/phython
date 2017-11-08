import random
minimum= int(input ("enter the lower range"))
maximum= int(input("enter higher range"))
maxTries = 5

myRandomNumber = random.randint (minimum, maximum)
theNumberGuessed = int (input("Guess a number between 1 and 6"))
tries = 0

while (tries < maxTries):
    if (theNumberGuessed != myRandomNumber):
        print ("incorrect : try again!")
        tries = tries+1
        theNumberGuessed = int( input("try again !:"))
        if(theNumberGuessed == myRandomNumber):
            print("wooohoo")
            exit (0)




