# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# Enter a file name: mbox-short.txt
# 04 3
# 06 1
...
# 18 1
# 19 1

fileOpen = open('mbox-short.txt')

timeDict = {}                                           # Declare dict to contain all (time, freq) values
timeList = []                                           # Decalre list to convert dict into sortable class

for line in fileOpen:                                   # Loops through text lines to extract relevant string lines
    words = line.split()
    if len(words) == 0 or words[0]!= 'From': continue   
    
    time = str(words[5])                                # Converts relevant string from lines into list
    pos1 = time.find(':')                               # Isolates hour from other time digits
    if time[:pos1] not in timeDict:                     # If else statement to add (time, freq) to dict
        timeDict[time[:pos1]] = 1                       
    else:
        timeDict[time[:pos1]] += 1
        
for key,val in list(timeDict.items()):                  # Loops through dict to append key-value items as tuples
    timeList.append((key,val))                          # Remember need to covnert key-value pairs as dict_items and convert dict into list
timeList.sort(reverse=False)                            

for key,val in timeList:                                # Loops through list of (time, freq) tuples and prints histogram
    print(key, val)


#Basically convert the time list into dict with freq to make histogram