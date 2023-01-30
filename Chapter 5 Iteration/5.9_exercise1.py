# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# average, max, and min of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

from statistics import mean
total = 0
numberSet = []

while True:
    try:
        number = input('Enter a number: ')
        if number == 'done':
            break
        number = float(number)
        numberSet.append(number)
        print(number)
    except:
        print('bad data')

try:        
    print('Count:', len(numberSet))
    print('Sum:', sum(numberSet))
    print('Mean:', mean(numberSet))
    print('Max:', max(numberSet))
    print('Min:', min(numberSet))
except:
    print('No Data input')
