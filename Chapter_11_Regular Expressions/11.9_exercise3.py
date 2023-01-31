# Exercise 3: Write a program using regex to extract all of the revision numbers 
# (the integer number at the end of these lines) from an mbox text file.

    # "Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772"
    # [39772]

import re

fileOpen = open('mbox-short.txt')

revNum = 'Details:.*rev=([0-9]+)'

for line in fileOpen:
    line = line.rstrip()
    x = re.findall(revNum,line)
    if len(x) > 0:
        print(x)
