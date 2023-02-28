class Pet:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    def speak(self):
        print('I don\'t know what to say')

class Cat(Pet):
    def speak(self):
        print('meow')

class Dog(Pet):  
    def speak(self):
        print('bark')

# When creating the sub-classes, we still insert the intialization of the same attributes
# inherited from the superclass. But instead of rewriting each attribute declaration, we can
# reference the super class attributes by using the super() method.
# Note we can continue to add more attributes.

class Fish(Pet):  
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}.')

f = Fish('bubbles', 1, 'orange')
f.show()