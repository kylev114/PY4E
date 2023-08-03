# TITLE: Rock Paper Scissors Game
# DESCRIPTION: Player chooses rock, paper, or scissors and competes with computer.
# DATE: 31JAN2023
moves = {'rock': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'paper' : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'scissors' : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

import random
try:
    player = input('Choose between: Rock, Paper, or Scissors\n').lower()

    print(f'You chose {player}! {moves[player]}')
except:
    print('You didn\'t choose a move. Try again')
    exit()

computer = random.choice(list(moves.keys()))

print(f'Computer chose {computer}! {moves[computer]}')

if player == computer:
    print('It\'s a tie!.')
else:
    if player == 'rock':
        if computer =='scissors': print('You win!')
        else: print('You lose')
    if player == 'scissors':
        if computer =='paper': print('You win!')
        else: print('You lose')
    if player == 'paper':
        if computer =='rock': print('You win!')
        else: print('You lose')
