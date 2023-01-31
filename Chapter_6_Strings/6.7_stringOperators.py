# The word in is a boolean operator that takes two strings and returns True if the
# first appears as a substring in the second:

print('a' in 'banana')
print('seed' in 'banana')

# The comparison operators work on strings.

word = 'banana'

if word == 'banana':
    print('All right, bananas.')

def compareToBanana(word):
    if word < 'banana':
        print('Your word, ' + word + ', is less than banana.')
    elif word > 'banana':
        print('Your word, ' + word + ', is greater than banana.')
    else:
        print('Your word, ' + word + ', is banana!.')

compareToBanana('apple')
compareToBanana('pineapple')
compareToBanana('Pineapple')

# Python does not handle uppercase and lowercase letters the same way that people
# do. All the uppercase letters come before all the lowercase letters. 
# A common way to address this problem is to convert strings to a standard format,
# such as all lowercase, before performing the comparison.

