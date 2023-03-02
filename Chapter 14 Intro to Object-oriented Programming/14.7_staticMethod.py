# Methods can be designated as object or class depending if it has self or class parameter. 
# A class method can access or modify the class state while a static method can’t access or modify it. 
# Static methods technically can exist outside classes, but are incorporated due to logical workflow. 
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
        fileOpen = open(file, 'r')
        fileRead = csv.DictReader(fileOpen)
        items = list(fileRead)
        
        for item in items:
                Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
                ) 

    @staticmethod
    def checkInt(num):
        '''We use 3 conditions because we consider .0 as int'''
        if isinstance(num,float): 
             return num.is_integer()
        elif isinstance(num,int): 
             return True
        else: 
             return False
            
print(Item.checkInt(5.0))
