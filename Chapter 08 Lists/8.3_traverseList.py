# The most common way to traverse the elements of a list is with a for loop. The
# syntax is the same as for strings:

cheeses = ['Cheddar', 'Edam', 'Gouda']

for cheese in cheeses:
    print(cheese)

# If you want to write or update the elements, you need the indices. 
# A common way to do that is to combine the functions range and len:

numbers = [17, 123, 25]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print(numbers[i])
print(numbers)

# Remember range function loops from 0 to parameter n-1. 
# So even though len(numbers) == 3, range(3) only outputs: 0, 1, 2, STOP!

# A list can contain another list, the nested list still counts as a single
#element. The length of this list is four:

listOfList = [1, [100,101,102], 3]

print(len(listOfList))
