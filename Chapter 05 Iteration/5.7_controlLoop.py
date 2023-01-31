# The pass statement is used as a placeholder for future code.
# When the pass statement is executed, nothing happens, 
# but you avoid getting an error when empty code is not allowed.

for x in [0, 1, 2]:
    pass

#The break keyword is used to end a loop in its current iteration.

for i in range(6):
    if i == 3:
        break
    print(i)

#The continue keyword is used to end a loop in its current iteration and continues to the next iteration.

for i in range(6):
    if i == 3:
        continue
    print(i)