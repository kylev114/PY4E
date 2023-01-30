# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary. (Remeber that strings are case sensitive!)

fileOpen = open('words.txt')

wordsDict = {}
for line in fileOpen:
    words = line.split()
    print('debug', words)
    for word in words:
        #print('debug', word)
        word = word.lower()
        if word not in wordsDict:
            wordsDict[word] = 1
        else:
            wordsDict[word] = wordsDict[word] + 1

    
#print(wordsDict)

print(wordsDict['we']) 