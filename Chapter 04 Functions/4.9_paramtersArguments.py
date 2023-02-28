# Inside the function, arguments are assigned to variables called parameters.
# This function assigns the argument to a parameter named bruce. 
# When the function is called, it prints the value of the parameter (whatever it is) twice.
# This function works with any value that can be printed.

def print_twice(bruce):
    print(bruce)
    print(bruce)

# Hint: Use ctrl + d to consecutively select successive the input argument bruce and change it quickly within the function

# This function works with any value that can be printed.

print_twice('Spam')

print_twice(17)

import math
print_twice(math.pi)

print_twice('Et Tu Brute? '*4)

statement = 'Stop Repeating Yourself'
print_twice(statement)

# Defined functions require each parameter to have an argument passes. 
# Without an argument, the function will display an error unless there is a default value specified:

def addTwo(x, y=0):
    print(x+y)

addTwo(5, 6)
addTwo(5)

# If there are an unknown amount of arguments, the special character *args is used.
# The following function has only one parameter palceholder which can take multiple arguments:


def myFun(*paramter):
    for argument in paramter:
        print(argument)
  
myFun('Hello', 'and', 'Goodbye')
