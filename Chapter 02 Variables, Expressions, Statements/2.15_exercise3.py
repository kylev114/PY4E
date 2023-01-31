# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

rate = int(rate)
hours = int(hours)

pay = hours*rate
print(pay)

pay = str(pay)
print('Pay: '+ pay)