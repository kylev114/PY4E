# Exercise 1: Read and parse the “From” lines of an mbox text file and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

fileOpen = open('mbox-short.txt')

emailDict = {}

for line in fileOpen:
    words = line.split()
    if len(words) == 0 or words[0]!= 'From': continue   

    if words[1] not in emailDict:
        emailDict[words[1]] = 1
    else:
        emailDict[words[1]] += 1
#print(emailDict)

emailList = []

for (key,val) in list(emailDict.items()):
    emailList.append((val,key))
emailList.sort(reverse=True)

[print(key, val) for (val, key) in emailList[:1]] 

# Even tho there's only one list element, the additonal loop reverses the order
    