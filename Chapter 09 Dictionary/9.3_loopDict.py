# If you use a dictionary as the sequence in a for statement, it traverses the keys of
# the dictionary. This loop prints each key and the corresponding value:

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

for key in counts:
    print(key, counts[key])

# Again, the keys are in no particular order.
# We can use this pattern to implement the various loop idioms that we have described earlier. 
# For example if we wanted to find all the entries in a dictionary
# with a value above ten, we could write the following code:

for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])

# If you want to print the keys in alphabetical order, you first make a list of the keys
# in the dictionary using the keys method available in dictionary objects, and then
# sort that list and loop through the sorted list, looking up each key and printing
# out key-value pairs in sorted order as follows:

countList = list(counts.keys())
countList.sort()

for key in countList:
    print(key, counts[key])

# Chapter 10 will explain how both the key-value pairs can be looped in a dict using tuples