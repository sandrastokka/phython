
theYearIEntered = int (input("please enter a year in the future"))
theYearIWasBornIn = int (input("please enter the year in witch you where born"))

print (type (theYearIEntered))
print (type (theYearIWasBornIn))

print ("My age in", theYearIEntered, "will be", theYearIEntered-theYearIWasBornIn)

#Tests
#nr 1) entered a string - breaks
#nr 2) enter a decimal - breaks
#nr 3) leave it empty - breaks
#nr 4) a space - breaks
