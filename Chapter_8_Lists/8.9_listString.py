# A string is a sequence of characters and a list is a sequence of values, but a list
# of characters is not the same as a string. To convert from a string to a list of
# characters, you can use list:

s = "'Tis but a scratch."
t = list(s)
print(t)

# The list function breaks a string into individual letters. If you want to break a
# string into list of words, you can use the split method:

s = "A SCRATCH? You arm's off"
t = s.split()
print(t)

# You can call split with an optional argument to change the default boundary ' ':

s = "No147852369it147852369isn't"
t = s.split("147852369")
print(t)

# join is a string method and the opposite of split and uses the list as the argument

t = ["Well", "whats","that", "then?"]
s = ' '
s = s.join(t)
print(s)

# The benefit of converting strings to list and vice versa
# is the different properties each class has. For example, 
# converting a string to a list allows you to now index your elements:

s = "I've had worse."
t = s.split()
print(t[2])

