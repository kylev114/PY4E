# If we want to extract data from a string in Python we can use the findall()
# method to extract all of the substrings which match a regular expression. Let’s use
# the example of wanting to extract anything that looks like an email address from
# while ignoring similiar. For example, we want to pull the email addresses
# from an mbox file:

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# The \S+ matches to as many non-whitespace characters as possible. 
# Since there two \S+ split at the '@', it searches for all text in 
# that field and ignores the @2PM.

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:          # findall() returns a list even if its empty, this removes those empty lists
        print(x)

# Note Some of our email addresses have incorrect characters like “<” or “;” 
# at the beginning or end. Square brackets are used to indicate a set of 
# multiple acceptable characters we are willing to consider matching:

subString = '[a-zA-Z0-9]\S*@\S*[a-zA-Z]'

# Translating this regular expression, we are looking for substrings that start 
# with a single lowercase letter, uppercase letter, or number “[a-zA-Z0-9]”, 
# followed by zero or more non-blank characters (\S*), 
# followed by an at-sign, followed by zero or more non-blank characters (\S*),
# followed by an uppercase or lowercase letter. Note that we switched from + to *
# to indicate zero or more non-blank characters since [a-zA-Z0-9] is already one
# non-blank character. Remember that the * or + applies to the single character
# immediately to the left of the plus or asterisk.

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall(subString, line)
    if len(x) > 0:
        print(x)