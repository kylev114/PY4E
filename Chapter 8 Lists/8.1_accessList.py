# Like a string, a list is a sequence of values.
# In a string, the values are characters, in a list, they can be any type.

x = [10, 20, 30, 40]
y = ['spam', 2.0, 5, [10, 20]]
z = []

# The syntax for accessing the elements of a list is the same as for accessing the
# characters of a string: the bracket operator. The expression inside the brackets
# specifies the index. Remember that the indices start at 0:

cheeses = ['Cheddar', 'Edam', 'Gouda']
print(cheeses[1])

# Unlike strings, lists are mutable because you can change the order of items in a
# list or reassign an item in a list.

numbers = [17, 123]
numbers[1] = 5
print(numbers)

# The in operator also works on lists:

if 'Cheddar' in cheeses:
    print('Cheddar is type of Cheese')
if 'Bananas' in cheeses:
    print('Bananas is type of Cheese')
