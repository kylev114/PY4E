# The __init__ method is specifically used to substantiate an object
# with attributes. Each attribute after the self-parameter will then need to
# be specified when constructing a new object instance.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age


myPet = Dog('Tim', 7)
yourPet = Dog('Bill', 4)

print(myPet.name)
print(yourPet.name)

# Instead of calling the attribute itself, it can be added to a method.
# This is useful when working with attributes. 

print(myPet.get_age())

yourPet.set_age(99)

print(yourPet.get_age())


