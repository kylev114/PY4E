# 14.2 reviewed exploring built-in objects along with their class and methods. 
# The class statement can be used to initialize a new class of objects.
# WIthin that initialization object methods and attributes can be defined. 


class Dog:
    def bark(self):
        print('bark')
    
    def convertAge(self,age):
        humanAge = age + 15
        return humanAge
    

    
myPet = Dog()               # create new instance of Dog class

print(type(myPet))          # main refers to the module the class was defined in (i.e. random objects in random module)

myPet.bark()                # calls the dog class method, bark(), onto variable 

x = myPet.convertAge(5)         # calls the method convertAge() and returns a value