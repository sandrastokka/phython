myNumber = int ((input ("Enter a number")))

sumOfdigits = 0

while myNumber > 0:
    sumOfdigits = sumOfdigits + myNumber % 10
    myNumber = int (myNumber/ 10)
    print ("sumOfDigits =", sumOfdigits, "myNumber = ", myNumber)

print ("sum of Digis is", sumOfdigits)
