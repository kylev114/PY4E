# It is tempting to use the operator on the left side of an assignment, with the
# intention of changing a character in a string. For example:

greeting = 'Hello, world!'
#greeting[0] = 'J' #returns an error

# The reason for the error is that strings are immutable, which means you can’t
# change an existing string. The best you can do is create a new string that is a
# variation on the original:

new_greeting = 'J' + greeting [1:]
print(new_greeting)

# This example concatenates a new first letter with a slice of greeting. It has no
# effect on the original string.

# Test other concatenations of slices to see how it interacts with the original string

new_greeting = 'J' + greeting [2:]
print(new_greeting)

new_greeting = 'J' + greeting [6:]
print(new_greeting)

new_greeting = 'J' + greeting [99:]
print(new_greeting)


