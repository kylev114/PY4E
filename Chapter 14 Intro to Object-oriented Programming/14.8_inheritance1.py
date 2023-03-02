# Inheritance is the concept that similiar classes with like methods and 
# attributes can be ordered into a hierachy of parent and sub-classes

# The following classes are very similiar with the same attributes:

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print('meow')

class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print('bark')

