# If we want to find numbers on lines that start with the string “X-...” such as:

# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000

# We can construct the following regular expression to select the lines:

subString = '^X-.*: [0-9.]+'

# Translating this, we are saying, we want lines that start with X-, followed by zero
# or more characters (.*), followed by a colon (:) and then a space. After the
# space we are looking for one or more characters that are either a digit (0-9) or
# a period [0-9.]+ 
# Note that inside the square brackets, the period matches an
# actual period (i.e., it is not a wildcard between the square brackets).

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search(subString, line):
        print(line)

# To extract only the numbers, we can use parentheses.
# Parentheses are another special character in regular expressions. When you add
# parentheses to a regular expression, they are ignored when matching the string:

subFloat = '^X\S*: ([0-9.]+)'

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall(subFloat, line)
    if len(x)> 0:
        print(x)

# Note that you must call the method findall() instead to indicate you only want a substring,
# not the whole string like in search(). 

