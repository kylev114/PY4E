# TITLE: Caeser Cipher
# DESCRIPTION: Encodes or decodes a given string of characters (non-case sensitive) using positional shift method
# DATE: 02Feb2023

import string

alphabet = list(string.ascii_lowercase)
position = list(range(26))
alphaDict=dict(zip(alphabet,position))

posChar = []        # list that holds position based on char value
userReturn = []     # list that holds encoded or decoded values

def encode(a):
    for letter in a: posChar.append(alphaDict[letter])           # creates list for position of given string based on 0-25
    for pos in posChar: userReturn.append(alphabet[(shift+pos)%26])   # replaces list with shifted characters; modulus 26 to account for looping
    return ''.join(userReturn)

def decode(a): 
    for letter in a: posChar.append(alphaDict[letter])           # creates list for position of given string based on 0-25
    for pos in posChar: userReturn.append(alphabet[(pos-shift)%26])   # replaces list with shifted characters
    return ''.join(userReturn)

userChoice = input('Would you like to encode or decode?\n')
userInp = input('What is your message? (non-case sensistive)\n').lower()
shift = int(input('How much would you like to shift?\n'))

if 'encode' in userChoice.lower():print('Your encoded message is:\n'+encode(userInp))
elif 'decode' in userChoice.lower(): print('Your decoded message is:\n'+decode(userInp))
else:
    print('Error, invalid input(s). Try again.')
    exit()


# Reflection:
# I ended up creating two for loops for each method as I did not find an efficient solution to 
# coordinate each letter and positional value with the dict. Making two lists and using their indexes 
# seemed easier.


