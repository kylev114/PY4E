# Python has a math module that provides most of the familiar mathematical functions. 
# Before we can use the module, we have to import it:

import math

# This statement creates a module object named math. If you print the module
# object, you get some information about it:

print(math)

# The module object contains the functions and variables defined in the module. To
# access one of the functions, you have to specify the name of the module and the
# name of the function, separated by a dot (also known as a period). This format is
# called dot notation.

example1 = 10 * math.log10(25)
print(example1)


# The first example computes the logarithm base 10 of 25. The
# math module also provides a function called log that computes logarithms base e.


radians = 0.7
height = math.sin(radians)
print(height)

# The second example finds the sine of radians. From the name of the variable you can tell
# that sin and the other trigonometric functions (cos, tan, etc.) take arguments in
# radians. To convert from degrees to radians, divide by 360 and multiply by 2π:

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))

# The expression math.pi gets the variable pi from the math module. The value of
# this variable is an approximation of π, accurate to about 15 digits.

# If you know your trigonometry, you can check the previous result by comparing it
# to the square root of two divided by two:

print(math.sqrt(2) / 2.0)