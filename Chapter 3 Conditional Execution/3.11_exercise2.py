# Exercise 2: Rewrite your pay program (exercise 3.1) using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the program:

try:
    hours = input('Enter Hours: ')
    hours = int(hours)
except:
    print('Error, please enter numeric input')
try:
    rate = input('Enter Rate: ')
    rate = int(rate)
except:
    print('Error, please enter numeric input')
    exit()

overtime = 0
overtimePay = 0

if hours > 40:
    overtime = hours - 40
    overtimePay = overtime * 1.5 * rate
    hours = hours - overtime

pay = hours*rate + overtimePay
print(pay)
pay = str(pay)
print('Pay: '+ pay)