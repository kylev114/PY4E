#Use dir function to display all built-in Python methods has for lists:

#print(dir(list))

# append adds a new element to the end of a list:

t = ['a', 'b', 'c']
t.append('100')
print(t)

# extend takes a list as an argument and appends all of the elements:

t1 = ['1', '2', '3']
t2 = ['98', '99']
t1.extend(t2) # Note that t2 is unchanged.
print(t1) 

# sort arranges the elements of the list from low to high:

x = ['d', 'c', 'e', 'b', 'a']
y = [1.0, 1, 99, 99.0]
x.sort()
y.sort()
print(x)
print(y)

# remove modifies the list and removes the element: 

t = ['a', 'b', 'c']
t.remove('b')
print(t)

# pop modifies the list and removes an element with an index parameter: 
# Note that it also returns the removed element.

t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

# The del statement can also be used to remove elements from a list:

t = ['a', 'b', 'c']
del t[1]
print(t)

t = [1, 2, 3, 4, 5, 6, 7]
del t[2:4]
print(t)
