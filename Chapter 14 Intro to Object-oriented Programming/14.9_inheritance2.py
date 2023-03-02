# We create a new parent (superclass) that has the same attributes as the two sub-classes.

class Pet:
    def __init__(self, name = 'no name', age = 0):
            self.name = name
            self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    def speak(self):
        print('I don\'t know what to say')

# We identify the parent class by passing it as a parameter;
# the Cat and Dog class inherit the Pet class. 

class Cat(Pet):
    def speak(self):
        print('meow')

class Dog(Pet):  
    def speak(self):
        print('bark')

# We can now construct an instance of the parent 
p = Pet('Tim', 19)
p.show()

# We construct an instances of a sub-class that inherited the properties of the parent
c = Cat('Bill', 34)
c.show()

d = Dog('Jill', 25)
d.show()

# Sub-classes can be used to contain more specific or different properties that overide parent.
c.speak()
d.speak()
p.speak()

# While coding we can use parent properties as placeholders for more sub-classes. 
# The sub-class will use missing attributes and methods of the parent class if not defined. 

class Fish(Pet):
    pass

f = Fish ("bubbles", 1)
f.speak()