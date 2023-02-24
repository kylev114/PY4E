# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

import re

fileOpen = open('mbox-short.txt')
dayDict = {}
for line in fileOpen:
    line = line.rstrip()
    if line.startswith('From ') == True: 
        line = line.split()
        line = re.findall('(@.+)',line[1])
        print(line)
        dayDict[line[0]] = dayDict.get(line[0], 0) + 1

print(dayDict)

