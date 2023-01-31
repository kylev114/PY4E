# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
# and create a function called computepay which takes two parameters (hours and rate).

a = input('Enter Hours: ')
b = input('Enter Rate: ')

def computepay(hours,rate):
    overtime = 0
    overtimePay = 0
    rate = int(rate)
    hours = int(hours)
    if hours > 40:
        overtime = hours - 40
        overtimePay = overtime * 1.5 * rate
        hours = hours - overtime
    pay = hours*rate + overtimePay
    pay = str(pay)
    return print('Pay: '+ pay)

computepay(a,b)
exit()