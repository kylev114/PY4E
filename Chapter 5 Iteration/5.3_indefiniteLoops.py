# We call the while statement an indefinite loop because it simply loops until some condition becomes False

# A way of writing useful loops is you can check the condition
# anywhere in the loop (not just at the top) and you can express the stop condition
# affirmatively (“stop when this happens”) rather than negatively (“keep going until
# that happens.”).

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

# Sometimes you are in an iteration of a loop and want to finish the current iteration
# and immediately jump to the next iteration. In that case you can use the continue
# statement to skip to the next iteration without finishing the body of the loop for
# the current iteration.

i = 0

while True:
    i = i + 1
    if i == 3:
        continue
    print(i)
    if i == 5:
        break

