# Suppose you are given a string and you want to count how many times each letter
# appears. There are several ways you could do it:

    # 1. You could create 26 variables, one for each letter of the alphabet. Then you
    # could traverse the string and, for each character, increment the corresponding
    # counter, probably using a chained conditional.

    # 2. You could create a list with 26 elements. Then you could convert each
    # character to a number (using the built-in function ord), use the number as
    # an index into the list, and increment the appropriate counter.
    
    # 3. You could create a dictionary with characters as keys and counters as the
    # corresponding values. The first time you see a character, you would add
    # an item to the dictionary. After that you would increment the value of an
    # existing item.

# The advantage of the dictionary implementation is that we don’t have to know ahead of time 
# which letters appear in the string and we only have to make room for the letters that do appear.
# Here is what the code might look like:

word = 'brontosaurus'
dInput = {}
for letter in word:
    if letter not in dInput:
        dInput[letter] = 1
    else:
        dInput[letter] += 1
print(dInput)

# We are effectively computing a histogram, which is a statistical term for a set of
# counters (or frequencies).

# Dictionaries have a method called get that takes a key and a default value. If the
# key appears in the dictionary, get returns the corresponding value; otherwise it
# returns the default value. For example:

age = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

print(age.get('jan'))
print(age.get('jan', 10))
print(age.get('kyle'))
print(age.get('kyle', 25))

# We can use get to write our histogram loop more concisely. Because the get
# method automatically handles the case where a key is not in a dictionary, we can
# reduce four lines down to one and eliminate the if statement"

word = 'brontosaurus'
dInput = dict()
for letter in word:
    dInput[letter] = dInput.get(letter,0)+ 1
print(dInput)
