# The __init__ method is specifically used to substantiate an instance
# with attributes. Each attribute after the self-parameter will then need to
# be specified when constructing a new object instance.

class Item:
    def __init__(self, name, price, quantity = 5):
        self.name = name
        self.price = price
        self.quantity = quantity
        print('Instance created at:', self)
        
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price


item1 = Item('phone', 500)
item2 = Item('computer', 800)

print(item1.name)
print(item2.name)

# Instead of calling the attribute itself, it can be added to a method (i.e. get_price()).
# This is useful when working with variable attributes. 

print(item1.get_price())
print(item2.get_price())

item1.set_price(999)
item2.set_price(item2.price*0.90)

print(item1.get_price())
print(item2.get_price())

# Of the three attributes, quantity has a preset value. 
# When contructing an instance, all of the attributes need to be defined
# except for quantity. It will be set to the default value unless specified.

item3 = Item('tv', 500, 7)
print(item3.quantity)



