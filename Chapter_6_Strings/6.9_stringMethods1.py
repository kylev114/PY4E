# Strings are an example of Python objects. An object contains both data (the actual
# string itself) and methods, which are effectively functions that are built into the
# object and are available to any instance of the object.

# Python has a function called dir which lists the methods available for an object.
# The type function shows the type of an object and the dir function shows the
# available methods.

stuff = 'hello world'
print(type(stuff))
print(dir(stuff))

help(str.upper)

# Calling a method is similar to calling a function (it takes arguments and returns
# a value) but the syntax is different. We call a method by appending the method
# name to the variable name using the period as a delimiter.

# Instead of the function syntax upper(stuff), we must uses the method syntax:
# stuff.upper()

new_stuff = stuff.upper()
print(new_stuff)

# The empty parentheses indicate that this method takes no argument. Some methods require arguments: 

o_stuff = stuff.find('o')
print(o_stuff)

# A method call is called an invocation:
# In the first case we invoke upper on stuff.
# In the second case we invoke find on stuff.
