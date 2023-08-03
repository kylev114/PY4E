# TITLE: BlackJack Game
# DESCRIPTION: Simulates blackjack game with user input for play against computer dealer.
# DATE: 06Feb2023

import random
import os

deck52 = []

def newDeck():
    '''Creates a new deck'''
    values = list(range(2,11)) + ['Jack', 'Queen', 'King', 'Ace']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    for value in values: 
        for suit in suits: deck52.append((value,suit))
    return

def drawCard ():
    '''Draws a random card from deck (does not replace the card).
    returns a tuple: (value, num/face, suit)'''
    card = deck52.pop(random.randint(0,len(deck52)-1))
    if isinstance(card[0], int) == False: value = 10
    else: value = card[0]
    if card[0] =='Ace': value +=1
    return (value, card[0], card[1])

def showdown():
    '''Compares player and computer hands and returns result'''
    if hand > 21: return print('You Lose.')
    if compHand > 21: return print('You Win!')
    if hand == compHand: return print('It\'s a tie!')
    if hand > compHand:return print('You Win!')
    else: return print('You Lose.')

if input('Welcome to the table, would you like to play blackjack? y or n\n').lower() == 'y': pass
else: 
        print("Ok, thanks for stopping by!")
        exit()

while True:  
    newDeck()

    # Player Hand
    print('Your cards are:')
    card1 = drawCard()
    card2 = drawCard()
    hand = card1[0]+card2[0]
    aceCount = 0
    if card1[1] == 'Ace': aceCount = 1
    if card2[1] == 'Ace': aceCount +=1
    print(f'{card1[1]} of {card1[2]} and {card2[1]} of {card2[2]}\n')

    # Computer Hand
    print('Computer drew a:')
    compCard1 = drawCard()
    compCard2 = drawCard()
    compHand = compCard1[0]+compCard2[0]
    compAceCount = 0
    if compCard1[1] == 'Ace': compAceCount = 1
    if compCard2[1] == 'Ace': compAceCount +=1
    print(f'{compCard1[1]} of {compCard1[2]} and another card.\n')

    # Player Plays Hand
    while True:
        if hand >21:
            if aceCount > 0:
                hand -= 10
                aceCount -=1
                continue
            print(f'Your hand is {hand} with {aceCount} aces\nBust!')
            break
        print(f'Your hand is {hand} with {aceCount} aces')
        if hand == 21:
            break
        if hand <= 20:
            if input('Hit or Stand? h or s\n').lower() == 'h':
                hitCard = drawCard()
                hand += hitCard[0]
                if hitCard[1] == 'Ace': aceCount += 1
                print(f'You draw {hitCard[1]} of {hitCard[2]}')
                continue
            else: break 

    # Computer Plays Hand  
    print(f'\nComputer reveals {compCard2[1]} of {compCard2[2]} for a hand of:\n{compHand} with {compAceCount} aces\n')
    while True:
        if hand >21:
            break
        if compHand >21:
            if compAceCount > 0:
                compHand -= 10
                compAceCount -=1
                continue
            print(f'Computer Busts!')
            break
        if compHand == 17 and hand<17: 
            print(f'Computer stands with {compHand}')
            break
        else:
            print(f'Computer has {compHand} and hits')
            print('Computer draws:')
            hitCard = drawCard()
            compHand += hitCard[0]
            if hitCard[1] == 'Ace': compAceCount = 1
            print(f'{hitCard[1]} of {hitCard[2]}\n')
            continue
        break 

    showdown()

    # Reset Game
    if input('Play Again? y or n\n').lower() == 'y': continue
    else: break

# Reflection:
# Decided to not spend too much time on this project; Could've incorporated balance, bet, split, doubles, and multiple players.
# More efficient to turn player play hand and computer play hand into single function call.
# Struggled trying to figure out a way to make a deck using dict and found list of tuple more efficient.
# Use time module to create more natural game pacing.
# Wanted to save time to continue progress and flesh out poker program instead.

#♠♥♦♣♤♡♧♢