# Construct logical expressions to strategically place a guard evaluation
# just before the evaluation that might cause an error using short circuit

#Case 1
x = 1
y = 1
case1 = x >= 0 and (x/y) >= 1
print(case1)

#Case 2
x = 1
y = 1
case2 = x >= 0 and (x/y) >= 2
print(case2)

#Case 3
x = 1
y = 0
case3 = x >= 0 and (x/y) > 2
print(case3)

# #Case 3 with guardian evaluation
# x = 1
# y = 0
# case3 = x >= 0 and y!=0 and (x/y) > 2
# print(case3)