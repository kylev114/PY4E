# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

word = 'racecar'
i = 1

while i <= len(word):
    letter = word[-i]
    print(letter)
    i = i+1