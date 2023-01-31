# Exercise 1: Rewrite your pay computation (exercise 2.3) to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
rate = int(rate)
hours = int(hours)

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