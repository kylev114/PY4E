# def is a keyword that indicates that this is a function definition. 
# The name of the function is print_lyrics. The empty parentheses after the name indicate that this function 
# doesn’t take any arguments. Later we will build functions that take arguments as their inputs.

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

# The value of print_lyrics is a function object, which has type “function”. 
# Using print() on a function will display function's identity, 
# in CPython implementation it's the address of the object in memory.

print_lyrics()
print(print_lyrics)
print(type(print_lyrics))

# Once you have defined a function, you can use it inside another function.

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

