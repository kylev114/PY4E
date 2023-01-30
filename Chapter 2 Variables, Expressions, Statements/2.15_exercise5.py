# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the 
# temperature to Fahrenheit, and print out the converted temperature.


tempC = input('What is the Clesius Temperature? \n')
tempC = int(tempC)
tempF = 1.8*tempC + 32
tempC = str(tempC)
tempF = str(tempF)
print('The temperature is '+tempC+' degrees Celsius'+' or '+ tempF + " degrees Farenheit" )