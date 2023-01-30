# Exercise 3: Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:

try:
    score = input('Enter score: ')
    score = float(score)
except:
    print('Error, please enter numeric input')
    exit()

if score > 0.9:
    grade = 'A'
elif score >= 0.8: 
    grade = 'B'
elif score >= 0.7: 
    grade = 'C'
elif score >= 0.6: 
    grade = 'D'
elif score < 0.6: 
    grade = 'F'

print(grade)