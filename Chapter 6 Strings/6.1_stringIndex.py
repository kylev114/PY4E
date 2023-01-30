# The expression in brackets is called an index. 
# The index indicates which character in the sequence you want (hence the name).

fruit = 'strawberry'
secondLetter = fruit[1]
firstLetter = fruit [0]

print(firstLetter)
print(secondLetter)

# To get the last character, you have to subtract 1 from the length:

length = len(fruit)
lastLetter = fruit[length - 1]

print(lastLetter)

# Alternatively, you can use negative indices, which count backward from the end of the string.
# -1 starts as the last, -2 is second to last and so on

firstToLastLetter = fruit[-1]
secondToLastLetter = fruit[-2]

print(firstToLastLetter)
print(secondToLastLetter)

# A traversal is a pattern of processing a string one character at a time. Often
# they start at the beginning, select each character in turn, do something to it, and
# continue until the end.

i = 0
while i < len(fruit):
    letter = fruit[i]
    print(letter)
    i = i + 1

# Another way to write a traversal is with a for loop:

for j in fruit:
    print(j)

