#defining a function
def celciusToFarenheit():
    myInput = int (input("enter a temprature in celcius:"))
    tempInFahrenheit = (myInput*9 + 160/5)
    print("The temp of " , myInput , "in celcius is" , tempInFahrenheit, "in Fahreihei")

#calling a function
celciusToFarenheit()
