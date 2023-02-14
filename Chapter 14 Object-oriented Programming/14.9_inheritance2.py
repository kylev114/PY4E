# We create a new superthat has the same attributes as the two sub-classes.

class Pet:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    def speak(self):
        print('I don\'t know what to say')
# We change the classes to take the superclass; we make the Cat and Dog class
# inherit the Pet class. 

class Cat(Pet):
    def speak(self):
        print('meow')

class Dog(Pet):  
    def speak(self):
        print('bark')

# We can now construct an instance of the superclass 
p = Pet('Tim', 19)
p.show()

# We construct an instances of a sub-class that inherited the properties of the superclass
c = Cat('Bill', 34)
c.show()

d = Dog('Jill', 25)
d.show()

# Note that sub-classes are used to contain more specific or different properties and overide super
c.speak()
d.speak()

p.speak()

# While coding we can use superclasses as placeholders for more sub-classes

class Fish(Pet):
    pass

f = Fish ("bubbles", 1)
f.speak()