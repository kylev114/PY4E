# Revisit 8.10 that looks for finding the day of the week using
# the line: "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# The original operation parses a string and coverts the result into a list.
# Change the operation to convert a string into a list to be parsed:

# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if words[0] !='From ': continue
#     print(words[2])

# Why is there an error? Debug to find out:

# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     print('debug', words)
#     if words[0] !='From ': continue
#     print(words[2])

# Note that when the program fails, the list of words is empty [].
# Refering to the text file, the error occurs when our program encounters 
# a blank line. You can use a guardian code to protect against lines which create empty lists:

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
