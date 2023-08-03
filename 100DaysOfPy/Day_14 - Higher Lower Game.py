
import random

import os
from rescBin import data, logo, vs

score = 0
reply = None

while True:   
    print(logo)

    if reply != None: print(reply)

    person1 = random.choice(data)
    person2 = random.choice(data)
    while person1 == person2: person2 = random.choice(data)

    print(person1['name'],'a', person1['description'], 'from', person1['country'])
    print(vs)
    print(person2['name'],'a', person2['description'], 'from', person2['country'])

    answer = input('Who has more followers? Pick A or B:').lower()
    print(answer)
    while True: 
        if answer == 'a' or 'b': break
        answer = input('Sorry please renter A or B. Or type "done" to end the game.').lower()

    if answer == 'a':
        if person1['follower_count'] > person2['follower_count']:
            score+=1
            reply=(f'Correct! Your Score is now: {score}')
        else: 
            reply=(f'Sorry that is Wrong! Your Score is: {score}') 

    elif answer == 'b':
        if person1['follower_count'] < person2['follower_count']:
            score+=1
            reply=(f'Correct! Your Score is now: {score}')
        else: 
            reply=(f'Sorry that is Wrong! Your Score is: {score}') 
    elif answer == 'done': break
    os.system('cls')
    


print(logo)
print(f'Game Over! Your final score is: {score}')

