# In 9.2 we created a histogram of each unqiue words using dict loop.
# What happens if we want to differentiate capitalization and punctuation?

# The .split() method uses empty character spaces as the splitter by default 
# so punctuation such as "soft!" is different from "soft." This can be solved 
# using translate() and maketrans() method:

# .translate(mapping_table)
# .maketrans(oldString, newString, deleteString) # mapping_table



import string
nonWords = string.punctuation + string.digits # string of all non-letter characters

fileOpen = open('romeo.txt')
fileDict = {}

for line in fileOpen:
    
    transStr = line.maketrans('','',nonWords)   # makes mapping table to replace all non-letter characters with empyty string: ''
    line = line.translate(transStr)             # applies mapping table onto each line of loop
    line = line.lower()                         # lowerscases each word to prevent duplicates ('I' == 'i')

    line = line.split()
    for word in line: fileDict[word] = fileDict.get(word,0)+1

print(fileDict)