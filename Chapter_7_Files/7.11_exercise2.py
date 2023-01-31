# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:

# 'X-DSPAM-Confidence: 0.8475'

# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

# Test your file on the mbox.txt and mbox-short.txt files.

from statistics import mean

try:
    fileName = input('Enter file Name: ')
    file = open(fileName)
except:
    print("Please Try Again")
    exit()

spamList=[] #create list to hold all of the spam numbers to be averaged

for i in file:
    if not i.startswith('X-DSPAM-Confidence:'): continue
    
# Locates out index of first digit in 'X-DSPAM...' string and stops loop onces its found
    for j, k in enumerate(i): 
        if k.isdigit():
            pos1 = j
            break

# extracts digit str from line, converts to float, and adds it to list
    spam = i[pos1:]
    spam = float(spam)
    spamList.append(spam)

# averages list and prints out average value
spamAverage = mean(spamList)
print('Average spam confidence:', spamAverage)
    
   
# helpful link for filtering the first digit in a string
# https://stackoverflow.com/questions/4510709/find-the-index-of-the-first-digit-in-a-string