# To find the largest value in a list or sequence, we can construct the following loop:

largest = 0
for i in [3, 41, 12, 9, 74, 15]:
    if largest is None or i > largest :
        largest = i
    print('Loop:', i, largest)
print('Largest:', largest)

# To compute the smallest number, the code is very similar with one small change:

smallest = None
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

# The built-in functions max() and min() make writing these exact loops unnecessary.



