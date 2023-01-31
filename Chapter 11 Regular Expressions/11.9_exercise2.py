# Exercise 2: Write a program to look for lines of the form:

    # "New Revision: 39772"

# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

import re
from statistics import mean 
fileOpen = open('mbox.txt')

subFloat = 'New Revision: ([0-9]+)'
revList = []

for line in fileOpen:
    line.rstrip()
    x = re.findall(subFloat,line)
    if len(x) > 0:
        revList.append(int(x[0]))

print(int(mean(revList)))
        