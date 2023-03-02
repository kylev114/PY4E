# Like attributes, methods can be distinguished between object methods and class methods.
# A class method uses cls as first parameter which references the class and not the instance (self).
# The method is also dressed with @classmethod line to siginify its use.

# The following creates 2 class methods
# The first method accesses the class and to return class attribute.
# The second class method adds data to a class attribute and is called within the class.

class Person:
    numberOfPeople = 0
    def __init__(self, name):
        self.name = name
        Person.addPerson()

    @classmethod
    def getNumberOfPeople(cls):
        return cls.numberOfPeople

    @classmethod
    def addPerson(cls):
        cls.numberOfPeople += 1

p1 = Person('tim')
p2 = Person('bill')


# The class attribute can be called from either the class or instance.

print(p1.numberOfPeople)
print(Person.numberOfPeople)

print(Person.getNumberOfPeople())
