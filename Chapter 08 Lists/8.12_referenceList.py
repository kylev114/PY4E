# If a refers to an object and you assign b = a, then both variables refer to the same object:

a = [1, 2, 3]
b = a

print(b is a)
print(b == a)

# The association of a variable with an object is called a reference. In this example,
# there are two references to the same object.
# An object with more than one reference has more than one name, 
# so we say that the object is aliased.

# If the aliased object is mutable, changes made with one alias affect the other:

b[0] = 17
print(a)

# Although this behavior can be useful but is error-prone if not accounted for:

x = 'banana'
y = x
x = 'apple'

print(y) 