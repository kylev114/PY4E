# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

fileOpen = open('mbox-short.txt')

dictLetter = {}
listLetter = []
nonLetters = string.punctuation + string.digits + string.whitespace     # variable to list all non-letters (space, punctuations, numbers)

for line in fileOpen:                                   
    line = line.strip()
    transStr = line.maketrans('', '', nonLetters)           # creates translating variable to translate all non-letters to empty string: ''
    line = line.translate(transStr)                         # applies translating variable onto string line
    line = line.lower()                                     # lowers all capitalization in string line                             

    for letter in line:                                     # Nested Loop that adds each string into dict with key-value of letter-freq
        if letter not in dictLetter: dictLetter[letter] = 1
        else: dictLetter[letter] += 1

[listLetter.append ((val,key)) for key,val in list(dictLetter.items())]     # converts dict of letters-freq into list of tuples
listLetter.sort(reverse=True)                                               # sorts from greatest to least freq
[print(key,val) for key,val in listLetter]                                  # prints resultant list of freq-letters from list
