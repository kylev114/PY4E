# When you pass a list to a function, the function gets a reference to the list. If
# the function modifies a list parameter, the caller sees the change. For example,
# delete_head removes the first element from a list:

def delete_head(alpha):
    del alpha[0]

numberList = [1,2,3]
delete_head(numberList)
print(numberList)

# The parameter alpha and the variable numberList are aliases for the same object.
# What happens if we use a slice instead of del statement?

def bad_delete_head(beta):
    beta = beta[1:] 
    

numberList = [1,2,3]
bad_delete_head(numberList)
print(numberList)

# The parameter alpha is not an alias for the object of the variable numberList. 
# The second function creates a new list (alpha) while the first function modifies it.

# It is important to distinguish between operations that modify lists and operations
# that create new lists. For example, the append method modifies a list, but the +
# operator creates a new list:

t1 = ['x', 'y']
t2 = t1.append('z')
print(t1)
print(t2)

t1 = ['x', 'y']
t2 = t1 + ['z']
print(t1)
print(t2)

# To fix the semantic error of the second function, you can work with the new list created
# instead of making the function modfy the list like the first function:

def fix_delete_head(gamma):
    gamma = gamma[1:]
    return gamma

numberList = [1,2,3]
newNumberList = fix_delete_head(numberList)
print(newNumberList)

# This may be a confusing idea. The best way to understand is to refer to how asignment operator works:

x = 1
x + 1        # >>> 1; this line does not modify x
x = x + 1    # >>> 2; this line creates a new variable but reuses x so the old x is replaced

