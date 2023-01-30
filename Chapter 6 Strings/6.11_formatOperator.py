# The format operator, % allows us to construct strings, replacing parts of the strings
# with the data stored in variables. When applied to integers, % is the modulus
# operator.

aNumber = 42
aString = '%d' % aNumber

print(aString)
print(type(aString))

aSentence = "The Ultimate Answer to Life, The Universe and Everything is... %d!" %aNumber 
print(aSentence)

# If there is more than one format sequence in the string, the second argument has
# to be a tuple. Each format sequence is matched with an element of the tuple, in order.

# The following example uses %d to format an integer, %g to format a floating-point
# number, and %s to format a string:

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))

# Make sure the number of elements in the tuple must match the number of format sequences
# in the string. The types of the elements also must match the format sequences.