# Syntactically, a tuple is a comma-separated list of values:

t0 = 'c', 'u', 'r', 'r' 'y'
print(t0)
print(type(t0))

# To create a tuple with a single element, you have to include the final comma:
# (Not doing so results in a string)

t1 = ('a',)

# Another way to construct a tuple is the built-in function tuple. With no argument,
# it creates an empty tuple:

t = tuple('curry')
print(t)

# Most list operators also work on tuples. The bracket operator indexes an element:

print(t[0])

print(t[1:3])

# If you try to modify one of the elements of the tuple, you get an error:

#t[0] = 'A'

# You can’t modify the elements of a tuple, but you can replace one tuple with
# another:

t = ('F',) + t[1:]

print(t)
