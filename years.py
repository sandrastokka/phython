currentYear = int(input("what year are we in now?"))
theYearIwasBorn = int (input ("please enter the year you where born"))
theYearIentered = int (input ("enter a year in the future"))
print ("My age in", theYearIentered, "will be", theYearIentered-theYearIwasBorn)
exit(0)

if(theYearIentered-theYearIwasBorn > 150):
    print("Im sorry to say that you are most likely dead")
exit(0)

if(theYearIwasBorn > currentYear):
    print ("your not yet born ")

if(theYearIwasBorn <= 1900):
    print ("thats too old!")
exit(0)

if(theYearIentered < theYearIwasBorn):
    print ("that make no sense")
exit(0)





