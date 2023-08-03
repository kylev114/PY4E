# TITLE: Password Generator Project
# DESCRIPTION: Returns a password based on number of letters, numbers, and symbols listed.
# DATE: 01Feb2023
import random
import string

random.seed(1)

letters =[]
numbers = []
symbols = []
password = []

# Retrieve characters and seperates them into lists
[letters.append(i) for i in string.ascii_letters]
[numbers.append(i) for i in string.digits]
[symbols.append(i) for i in string.punctuation]


print("Welcome to the PyPassword Generator!")

#Prompt user input for number of each character
numLetters= int(input("How many letters would you like in your password?\n")) 
numNumbers = int(input(f"How many numbers would you like?\n"))
numSymbols = int(input(f"How many symbols would you like?\n"))

# Add randomcharacter based on user input to password list
[password.append(random.choice(letters)) for i in range(numLetters)]
[password.append(random.choice(symbols)) for i in range(numSymbols)]
[password.append(random.choice(numbers)) for i in range(numNumbers)]

# Randomize password list Order
random.shuffle(password)
print(''.join(password))
