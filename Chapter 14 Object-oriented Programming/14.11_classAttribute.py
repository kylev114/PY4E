# 14.5 and 14.6 created methods and attributes for class instance, not the 
# class itself. A class attribute can be create outside of the def statement:

class Person:
    numberOfPeople = 0
    def __init__(self, name):
        self.name = name
        self.addPerson()

    @classmethod
    def getNumberOfPeople(cls):
        return cls.numberOfPeople

    @classmethod
    def addPerson(cls):
        cls.numberOfPeople += 1



# The class attribute can be called from either the class itself or an instance of the class.
# Note that when each instance is constructed, it changes the 
print(Person.numberOfPeople)

p1 = Person('tim')
print(p1.numberOfPeople)

p2 = Person('bill')
print(p2.numberOfPeople)


# When defining class methods, we use @classmethods to dress the method
print(Person.numberOfPeople)
