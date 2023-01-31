# Exercise 1: Write a function called modify_list that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called create_new_list that takes a list and returns a new list that
# contains all but the first and last elements.

x = [1,2,3]
y = ['a','b','c']

def modify_list(s):
    t = s
    del t[0]
    del t[-1]
    return None

def create_new_list(s):
    s = s[1:]
    return s

modify_list(x)
print(x)

y = create_new_list(y)
print(y)

# Note how the first function still affects the variable x as list objects are mutable;
# parameter s and variable t aliases with variable x