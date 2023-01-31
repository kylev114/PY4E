# There are a number of other special characters that let build powerful
# regular expressions. For example, the carot or '^' character can be used 
# with the search regular expression to indicate only strings that start
# with the specified parameter field:

import re
hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)


# The most commonly used special character is the period or
# full stop, which matches any character.

# In the following example, the regular expression F..m: would match any of the
# strings such as “From:”, “Fxxm:”, “F12m:”, or “F!@m:” since the period characters in the
# regular expression match any character.

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# This can be combined with the * or + action characters into a
# the regular expression. These special characters mean that instead of matching a single
# character in the search string, they match zero-or-more characters (in the case of
# the asterisk) or one-or-more of the characters (in the case of the plus sign).

# Search for lines that start with From and have an at sign
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)

# 'ab+' will match ‘a’ if there is at least 1 or more ‘b’s , it will not match just ‘a’
# 'ab*' will match ‘a’ and any ‘b’s if present, it can match just ‘a’