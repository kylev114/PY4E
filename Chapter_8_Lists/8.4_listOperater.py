# The + operator concatenates lists:

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# The * operator repeats a list a given number of times:
i = [0]
j = [1,99]
print(i*4)
print(j*4)

# The slice operator sublists lists: 
# Remember the first parameter is inclusive and second is exclusive

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:3])
print(t[:])

# Also remember that lists are mutable and that includes slices:

t[1:3] = ['x', 'y']
print(t)