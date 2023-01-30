# For loops can take a tuple assignment with a dictionary items() method. 
# This allows traversing the keys and values of a dictionary in a single loop.

d = {'apples':10, 'oranges':5, 'bananas':20,}

for (key, val) in list(d.items()):
    print(val,key)

# This loop has two iteration variables because list(items.()) returns a list of tuples and
# (key, val) is a tuple assignment that successively iterates through each of the key-value
# pairs in the dictionary (still in hash order; no particular order).

# Tuple items can be appended onto a list using this for loop iteration.
# If the tuples are key-value pairs, it can effectively be done to sort a dict:

originalDict = {'broccoli':2, 'carrots':6, 'onions':4}
outputList = []

for (key, val) in list(originalDict.items()):
    outputList.append((key,val)) # make sure to specify it is only a "single" element being added

outputList.sort()
print(outputList)

