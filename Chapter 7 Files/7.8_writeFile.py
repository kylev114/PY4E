# To write a file, you have to open it with mode “w” as a second parameter.
# If the file already exists, opening it in write mode clears out the old data and starts
# fresh, so be careful! If the file doesn’t exist, a new one is created.

fout = open('output.txt', 'w')
print(fout)

# The write method of the file handle object puts data into the file, returning the
# number of characters written. The default write mode is text for writing (and
# reading) strings.

line1 = "This here's the wattle,\n"
fout.write(line1)

# Calling write again adds new data to the end

line2 = 'the emblem of our land.\n'
fout.write(line2)

# repr takes any object as an argument and returns a string representation of the object
# which can help avoid problems with whitespace or \ characters in text.
# These errors can be hard to debug because spaces, tabs, and newlines are
# normally invisible:

s = '1 2\t 3\n 4'
print(s)

print(repr(s))

# Python automatically closes files that are open when the program ends 
# but its good practice as more complicated programs with multiple files 
# might interfere with each other.

fout.close()
