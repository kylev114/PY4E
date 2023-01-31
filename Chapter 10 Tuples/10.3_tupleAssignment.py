# Python language has the ability to have a tuple on the left side 
# and a sequence on the right side of an assignment statement.
# This allows you to assign more than one variable at a time to the given sequence.

m = ['have', 'fun']

x, y = m

print(x)
print(y)

# Application of tuple assignment allows us to swap the values of two variables in a single statement:

a = 5
b = 7

a , b = b, a

print(a)
print(b)

# The number of variables on the left and the number of values on the right must be
# the same:

#a, b = 1, 2, 3

# The right side can be any kind of sequence (string, list, or tuple).
# For example, to split an email address into a user name and a domain, you could
# write:

address = 'monty@python.org'
userName, domain = address.split('@')
print(userName+'\n'+domain)