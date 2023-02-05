# Exercise 4: Add code to the exercise 9.3 to figure out who has the
# most messages in the file. After all the data has been read and the 
# dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.


fileOpen = open('mbox-short.txt')
dayDict = {}

for line in fileOpen:
    line = line.rstrip()
    if line.startswith('From ') == True: 
        line = line.split()
        dayDict[line[1]] = dayDict.get(line[1], 0) + 1

emailName = None
emailFreq = None

for email in dayDict:
    if emailFreq == None or dayDict[email] > emailFreq:
        emailName = email
        emailFreq = dayDict[email]

print(emailName, emailFreq)
