# Class methods are useful for accessing and using class data.
# Adding data to a class is commonly done using a class method.
# The following uses csv file created from 14.4
import csv

class Item:
    all = []
    itemCount = 0
    def __init__(self, name = 'invalid', price = "n/a", quantity = "n/a"):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        print('Instance created:', self) 

    def __repr__(self):
        return f'Item({self.name},{self.price},{self.quantity})'

    @classmethod
    def instantiate_from_csv(cls, file):  
        # Opens specfied csv file and converts it into list of dict items
        fileOpen = open(file, 'r')
        fileRead = csv.DictReader(fileOpen)
        items = list(fileRead)
        
        #Constructs class instance for each element in list of data from csv file
        for item in items:
                Item(
                name = item.get('name'),
                price = int(item.get('price')),
                quantity = int(item.get('quantity'))
                )           

# We can import the csv module which works with csv files more efficiently.
# The items.csv file can be extracted for the data to construct instances for the Item class.

Item.instantiate_from_csv("items.csv")

# Each object instance is stored in the class attribute all list.
print(Item.all)
print(Item.all[0].price)
