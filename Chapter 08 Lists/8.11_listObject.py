# In python, if we create two variables with the same string, they are equal:

a = 'apple'
b = 'apple'

print(a is b)
print(a == b)


# Doing the same thing except with list leads to a different result:

x = [1,2,3]
y = [1,2,3]

print(x is y)
print(x == y)

# In the second case, a and b refer to two different objects that have the same value. 
# But in the first case, they refer to the same object. The comparator operator == shows 
# a and b reference objects of equal value, but the 'is' operator shows the objects 
# are not the same.

# A specific list is a unique object that can share the same value with other lists
# Until now, we have been using “object” and “value” interchangeably, but it is more
# precise to say that an object has a value.

