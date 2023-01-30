# Exercise 4: 
# Write a function that opens a text file and reads it line by line. 
# For each line, split the line into a list of words using the split function. 
# For each word, check to see if the word is already in the list of unique words. 
# If the word is not in the list of unique words, add it to the list.
# Make sure there are no duplicate words in the list.
# When the fnction completes it sorts and returns
# the list of unique words in alphabetical order:

# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

userInput = input('Enter file: ')
fileOpen = open(userInput)

def uniqueWords():
    wordList =[]
    for line in fileOpen:
        words = line.split()
        for i in words:
            if i not in wordList:
                wordList.append(i)
    wordList.sort()
    return wordList

print(uniqueWords(fileOpen))