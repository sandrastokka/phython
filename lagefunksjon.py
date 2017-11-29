#defining a function
def farenheitToCelcius():
    fahrenheit = int (input ("What fahrenheit temperature do you want to convert? :"))
    print
    celcius =((fahrenheit -32/9)*5)
    print( fahrenheit, celcius , "celcius")




optionSelected = input ("do yo want to convert from celcius to fahrenheit or fahrenheit to celcius? write C for celcius to fahrenheit and F for fahrenheit to celcius"
       "")
print

if(optionSelected == "f"):
    farenheitToCelcius()

import turtle

