# Dictionaries have a method called items that returns a class called dict_items which contains
# tuple of each key-value pair:

d = {'apples':10, 'oranges':5, 'bananas':20,}
t = d.items()
print(t)
print(type(t),)

# The items are in no particular order and ce can make convert the dict_list of tuples into  
# the list, Since lists are mutable, we can now use the sort method: 

t = list(t)
t.sort()
print(t)

# For loops can take items method and  tuple assignment. 
# This allows traversing the keys and values of a dictionary in a single loop

for key, val in list(d.items()):
    print(val,key)
