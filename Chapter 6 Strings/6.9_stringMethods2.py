word = 'banana'

#Some method optionally require arguments, and/or take more than 1 at a time:

new_word = word.find('na')
print(new_word)

new_word = word.find('na', 3)
print(new_word)

new_word = word.find('apple')
print(new_word)

# One common task is to remove white space (spaces, tabs, or newlines) from the
# beginning and end of a string using the strip method:

line = '            Here we go              '
new_line = line.strip()
print(new_line)

# Some methods such as startswith return boolean values.

line = 'Have a nice day'
true_line = line.startswith('Have')
print(true_line)
flase_line = line.startswith('h')
print(flase_line)

# Methods can also be called together in the same expression using the dot notation:

fixed_line = line.lower().startswith('h')
print(fixed_line)