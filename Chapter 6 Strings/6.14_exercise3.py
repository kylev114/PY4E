# Exercise 3: Define a function called countLetter that counts number of times a letter appears in a string. 
# Make the function accept the string and a letter as arguments.

def countLetter(word, letter):
    counter = 0
    for i in word:
        if i == letter:
            counter = counter + 1
    #return counter

a = countLetter('banana','a')

b = countLetter('alphabet', 'a')

print(a)
print(b)