# TITLE: Tip Calculator
# DESCRIPTION: Calculates bill per person based on total bill, number or people, and tip.
# DATE: 31Jan2023

bill = float(input('Enter your bill: '))
people = int(input('Enter your party size: '))
tip = float(input('Enter tip percentage as decimal: '))

cost = bill/people*tip

print('Each person pays: $%.2f'%cost)