# TITLE: Number Guess
# DESCRIPTION: Creates a game where user must guess a a random number from 1 to 100
# with limited chances. Returns if guess was too high or low
# DATE: 08 Feb 2023

import random

def resetGame():
    print('I\'m thinking of a number between 1 and 100.')
    return random.randint(1,100)

num = resetGame()

if input('Can you guess it? y or n\n').lower() == 'n':
    print('Maybe next time!')
    exit()
else:
    if input('Would you like to make this hard? y or n\n').lower() == 'y': lives = 5
    else: lives = 10

while True:
    guess = int(input('What is your guess?\n'))
        
    if guess > num: print('Too High!')
    if guess < num: print('Too Low!')
    if guess == num:
        print('Correct!\nYou Win')
        if input('Play Again? y or n\n').lower() == 'y': 
            num = resetGame()
            continue
        else: exit()
    
    lives -= 1
    
    if lives == 0:
        print('No More Guesses!')
        if input('Play Again? y or n\n').lower() == 'y': 
            num = resetGame()
            continue
        print('See ya!')
        exit()

    print(f'You have {lives} guesses left')


