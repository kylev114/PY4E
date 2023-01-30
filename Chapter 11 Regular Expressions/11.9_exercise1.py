# Exercise 1: Write a simple function to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression
# import re

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-

# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$

import re
fileOpen = open('mbox.txt')

def regexCounter(a):
    count = 0
    for line in fileOpen:
        line.rstrip()
        if re.search(a,line):
            count +=1
    return count 

regexInput = input('Enter a regular expression: ')
print('mbox.txt had', regexCounter(regexInput),'lines that matched', regexInput)