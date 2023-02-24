# Python has built-in objects.
# Here is a familiar example:

stuff = list()                      # constructs an object of type list

# Remember that we can take a use dir() function to return list of
# different methods an object has:

print(dir(stuff))

# The following are examples of calling methods to an object:

stuff.append('python')              # calls the append() method on object
stuff.append('chuck')               # calls the append() method on object
stuff.sort()                        # calls the sort() method on object
print (stuff[0])                    # retrieves item at index position 0
print (stuff.__getitem__(0))        # cals __getitem__() method with parameter 0
print (list.__getitem__(stuff,0))   # alternative way to use __getitem__() specifying list object



