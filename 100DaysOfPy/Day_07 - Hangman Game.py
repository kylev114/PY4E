# TITLE: Hangman Game
# DESCRIPTION: Interactive hangman game with given word list of various animals.
# DATE: 02Feb2023

from rescBin import hangmanAscii # retrieve ASCII art from resource bin
from rescBin import words        # imports list of random animal names
import random


randWord = list(random.choice(words))
blank = list('_'*len(randWord))
wordBank = []
lives = 0

print('Word:',''.join(blank))
answer = ''.join(randWord)
while "_" in blank:
    
    guess = input('Guess a Letter:\n')
    if len(guess) == 1: wordBank.append(guess)
    wrongAnswer = True

    for i in range(len(randWord)):
        if guess == randWord[i]:
            blank[i] = randWord[i]
            wrongAnswer = False
    
    if wrongAnswer==True: lives +=1

    print(hangmanAscii(lives),'\n\n')    
    print('Word:',''.join(blank))
    print('Word Bank: ',' '.join(wordBank))

    if lives == 6:
        print(f'You Lose!\nAnswer: {answer}')

        exit()
    
print('You Win!')

    


