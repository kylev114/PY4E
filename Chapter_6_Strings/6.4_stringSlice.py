# A segment of a string is called a slice. Selecting a slice is similar to selecting a
# character:

s = 'Monty Python' #len(s) = 12

print(s[0:5])
print(s[6:12])

# The operator [n:m] returns the part of the string from the “n-th” character to the
# “m-th” character, including the first but excluding the last.

# If you omit the first index (before the colon), the slice starts at the beginning of
# the string. If you omit the second index, the slice goes to the end of the string. 
# If there is just a colon the index selects all:

fruit = 'strawberry'

print(fruit[:5])
print(fruit[5:])
print(fruit[:]) #selects all

print(fruit[5:5]) #index are equal so ouput is an empty string
print(fruit[1:0]) #first index is >second so output is an empty string

# An empty string contains no characters and has length 0, but other than that, it
# is the same as any other string