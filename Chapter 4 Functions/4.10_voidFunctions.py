def print_twice(bruce):
    print(bruce)
    print(bruce)

# Void functions might display something on the screen or have some other effect,
# but they don’t have a return value. If you try to assign the result to a variable,
# you get a special value called None

result = print_twice('Bing')
print(result)

# To return a result from a function, we use the return statement in our function.
# For example, we could make a very simple function called addtwo that adds two
# numbers together and returns a result

def addtwo(a, b):
    sum = a + b
    return sum

x = addtwo(3, 5)
print(x)

