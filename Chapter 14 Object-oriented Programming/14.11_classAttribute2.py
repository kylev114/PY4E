# 14.5 and 14.6 created an methods and attributes for class instance, not the 
# class itself. 

class Person:
    numberOfPeople = 0

    def __init__(self, name):
        self.name = name
        #self.addPerson()

    @classmethod
    def getNumberOfPeople(cls):
        return cls.numberOfPeople

    @classmethod
    def addPerson(cls):
        cls.numberOfPeople += 1

# The class attribute can be called from both the class or class instance
p1 = Person('tim')
p2 = Person('bill')

print(p1.numberOfPeople)
print(p2.numberOfPeople)
print(Person.numberOfPeople)

# When defining class methods, we use @classmethods to dress the method
print(Person.getNumberOfPeople())
