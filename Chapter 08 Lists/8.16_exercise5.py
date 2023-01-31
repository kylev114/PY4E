# Exercise 5: Write a program to read through the mail box data and when you find
# line that starts with “From”, you will split the line into words using the
# split function. We are interested in who sent the message, which is the
# second word on the From line.
# Parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:)
# lines and print out a count at the end. 

# Enter a file name: mbox-short.txt
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# There were 27 lines in the file with From as the first word


fhand = open('mbox-short.txt')

counter = 0

for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    counter = counter + 1
    print(words[1])
print ('There were', counter, 'lines in the file with From as the first word')