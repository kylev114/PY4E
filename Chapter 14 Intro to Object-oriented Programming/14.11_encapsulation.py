# Encapsulation is one of the key features of object-oriented programming. 
# It refers to the bundling of attributes and methods inside a single class.
# It prevents outer classes from accessing and changing attributes and methods of a class.
# This also helps to achieve data hiding.

# Private variables and methods are denoted using underscore as a prefix:
# i.e. __variable or __method

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# change the price using setter function
c.setMaxPrice(1000)
c.sell()

# We cannot modify the value of __maxprice outside of the class.

# To modfiy the private variable, we have to use a setter function i.e setMaxPrice()
# The setter function is within the class and takes price as a parameter.
# Ommission of a setter or getter function is done for "read-only" attributes