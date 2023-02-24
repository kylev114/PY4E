# One of the common uses of a dictionary is to count the occurrence of words in a
# file with some written text. Let’s start with a very simple file of words taken from
# the text of Romeo and Juliet.

fileOpen = open('romeo.txt')

fileDict = {}

for line in fileOpen:
    line = line.split()
    #print(line)
    for word in line: fileDict[word] = fileDict.get(word,0)+1

print(fileDict)