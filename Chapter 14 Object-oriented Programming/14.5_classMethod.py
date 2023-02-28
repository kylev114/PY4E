# Like attributes, methods can also be distinct between object methods and class methods.
# A class method uses cls as first parameter which references the class and not the instance.
# The method is also dressed @classmethod line before it to siginify its use.

import csv

class Item:
    all = []
 
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

# The data for each item of the csv file has been constrcuted as as class instance without needing to
# individually declare each as a variable in a seperate line. The data is stored in the class list. 

print(Item.all)
print(Item.all[0].price)

# Althought everything may seem redundant or unecessary, understand that the data can now be
# controlled and manipulated with OOP concepts. 