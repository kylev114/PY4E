# Sometimes we need to use regex to search for characters 
# that are being used by regex special characrters (i.e. $, +, *, etc.).
# To do so simply prefix with '\' backslash 
# to inidcate that the following character is not a special character:

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)

print(y)

# Note the period is also inside the bracket which reverts it to its default character.
