# 14.2 reviewed exploring built-in objects along with their class and methods. 
# The class statement can be used to initialize a new class of objects.
# Within that initialization object methods and attributes can be defined. 


class Dog:
    def bark(self):
        print('bark '*2)
    
    def convertAge(self,age):
        humanAge = age + 15
        return humanAge
    

    
myPet = Dog() # create new instance of Dog class

# We can see the new object instance defined and use the type and dir functions.
# __main__ refers to the module the class was defined in (i.e. random objects in random module).
# Note that within the directory are built in-in methods as well as the custom defined ones.

print('Type', type(myPet))     
print('Directory', dir(myPet))     

# New methods can be added to the class declaration using def
# to create a function. The work the same as built-in methods.

myPet.bark()                

# Note that each def method requires a self parameter 
# before other parameters are introduced. 

print(myPet.convertAge(5))
