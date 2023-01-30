# A dictionary is like a list, but more general. In a list, the index positions have to
# be integers; in a dictionary, the indices can be (almost) any type.

# You can think of a dictionary as a mapping between a set of indices (which are
# called keys) and a set of values. Each key maps to a value. The association of a
# key and a value is called a key-value pair or sometimes an item.

# The function dict creates a new dictionary with no items:

eng2sp = dict()
print(eng2sp)

# To add items to the dictionary, you can use square brackets:

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

# The order of the key-value pairs is not the same. In fact, if you type the same
# example on your computer, you might get a different result. In general, the order
# of items in a dictionary is unpredictable.

# But that’s not a problem because the elements of a dictionary are never indexed
# with integer indices. Instead, you use the keys to look up the corresponding values:

print(eng2sp['two'])

# The len() function can count the number of key-value pairs:

print(len(eng2sp))

# The in operator can tell if a key apears in a dictionary:

print('one' in eng2sp)

print('uno' in eng2sp)

# To see whether something appears as a value in a dictionary, you can use the
# method values, which returns the values as a type that can be converted to a list,
# and then use the in operator:

englishSpanish = list(eng2sp.values())
print('uno' in englishSpanish)
