# Exercise 3: Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.


fileOpen = open('mbox-short.txt')
dayDict = {}
for line in fileOpen:
    line = line.rstrip()
    if line.startswith('From ') == True: 
        line = line.split()
        dayDict[line[1]] = dayDict.get(line[1], 0) + 1
print(dayDict)

