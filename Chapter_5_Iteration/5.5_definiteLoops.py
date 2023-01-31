# We call the for loop a definite loop, its used for iterating
# over a sequence such as list, a tuple, a dictionary, a set, or a string.
# It runs through as many iterations as there are items in the set.

friends = ['Joseph', 'Glenn', 'Sally']
for i in friends:
    print('Happy New Year:', i)
print('Done!')

# The variable friends is a list of three strings, i is the iteration variable for the for loop. 
# The variable i# changes for each iteration of the loop and controls when the for loop completes.
# The iteration variable steps successively through the three strings stored in the friends variable.

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

# Our iteration variable is named itervar and
# while we do not use itervar in the loop, it does control the loop and cause the
# loop body to be executed once for each of the values in the list.

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)

# In this loop we do use the iteration variable. Instead of simply adding one to the
# count as in the previous loop, we add the actual number (3, 41, 12, etc.) to the
# running total during each loop iteration. 
# As the loop executes, the variable total accumulates the sum of the elements; a variable used
# this way is sometimes called an accumulator.

# These loops are for demonstration purposes and mimic the simpler len() and sum() functions.