# The __init__ method is specifically used to substantiate an instance
# with attributes. Each attribute after the self-parameter will then need to
# be specified when constructing a new object instance.

class Item:
    def __init__(self, name, price, quantity = 5):
        self.name = name
        self.price = price
        self.quantity = quantity
        print('Instance created:', self) # self will return the object location
        
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price

    def total_value(self):
        return self.price * self.quantity
    
# When construcuting a class instance, we must specify each parameter if 
# there is no default value just like with function parameters.

item1 = Item('phone', 500)
item2 = Item('computer', 800, 2)

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




