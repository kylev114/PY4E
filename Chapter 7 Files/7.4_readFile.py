# While the file handle does not contain the data for the file, it is quite easy to
# construct a for loop to read through and count each of the lines in a file:

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# When the file is read using a for loop in this manner, Python takes care of splitting
# the data in the file into separate lines using the newline character. Python reads
# each line through the newline and includes the newline as the last character in the
# line variable for each iteration of the for loop

# Because the for loop reads the data one line at a time, it can efficiently read and
# count the lines in very large files without running out of main memory to store
# the data. 

# If you know the file is relatively small compared to the size of your main memory,
# you can read the whole file into one string using the read method on the file handle.

fhand = open('mbox-short.txt')
shortFile = fhand.read()
print(len(shortFile))
print(shortFile[:20])

# In this example, the entire contents (all 94,626 characters) of the file mbox-short.txt
# are read directly into the variable shortFile. We use string slicing to print out the first
# 20 characters of the string data stored in shortFile.

# When the file is read in this manner, all the characters including all of the lines
# and newline characters are one big string in the variable shortFile. It is a good idea
# to store the output of read as a variable because each call to read exhausts the
# resource:

print(len(fhand.read()))
print(len(fhand.read()))
print(len(fhand.read()))

# From above, the read resource fails as it has reached its max memory in python (line 23). 
# # open function should only be used if the file data
# will fit comfortably in the main memory of your computer. If the file is too large
# to fit in main memory, you should write your program to read the file in chunks
# using a for or while loop.