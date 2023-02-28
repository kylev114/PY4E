# Classes can hold their own attributes by initializing them outside the __init__

class Item:

    discount = 0.8
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        print('Instance created:', self) 

    def apply_discount(self):
        print(self.price * self.discount)
        #print(self.price * Item.discount)
        return
    
    def __repr__(self):
        return f'Item({self.name},{self.price},{self.quantity})'


item1 = Item('phone', 100, 2)
item2 = Item('computer', 100, 5)
item3 = Item('camera', 1000, 8)
item4 = Item('tv', 100, 10)

# Note that instances are under the class umbrella so they contain the class attribute as well.
# The instance-level supesedes the class if called on specifically but will not change it at the class-level.
# See the difference within the apply_discount() method:

item1.apply_discount()

item2.discount = 0.9
item2.apply_discount()

# Class attributes can be useful ways to control the data within them.
# By making a class-level list, each instance can be appended and easily extracted for data:

for instance in Item.all:
    print(f'{instance.name} located at {instance}')

# Note that returning the instance (or self) gives object location which is sometimes hard to use. 
# Represent objects of a class for better usability by using __repr__ method.
# This method returns a string containing a printable representation of the object.

# When __repr__  is used in a class method, each instance construction is represented with a specified string. 
# Thus whenever an object is referenced, this string will be used instead of default object location. 
# A good documentation technique is to use csv (Comma Seperated Values) which allows for easy data file transfering.
# The list of object instances of the class can now be extracted onto a .csv file:

print(Item.all)

fileOpen = open('items.csv', 'w')
fileOpen.write("name,price,quantity\n") # creates header for csv table

for line in Item.all:
    fileOpen.write(str(line)+"\n")

