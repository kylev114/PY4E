# If we wanted to read a file and only print out lines which started with
# the prefix “From:”, we could use the string method startswith to select only those
# lines with the desired prefix:

fhand = open('mbox-short.txt')
for line in fhand:
        if line.startswith('From:'):
            print(line)

# The output looks great since the only lines we are seeing are those which start with
# “From:”, but why are we seeing the extra blank lines? This is due to that invisible
# newline character. Each of the lines ends with a newline, so the print statement
# prints the string in the variable line which includes a newline and then print adds
# another newline, resulting in the double spacing effect we see

# You can use the rstrip method which strips whitespaces from the right side of a string:

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# As your file processing programs get more complicated, you may want to structure
# your search loops using continue. The basic idea of the search loop is that you are
# looking for “interesting” lines and effectively skipping “uninteresting” lines. And
# then when we find an interesting line, we do something with that line.

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # Process our 'interesting' line
    print(line)

# We can use the find string method to simulate a text editor search that finds lines
# where the search string is anywhere in the line. Since find looks for an occurrence
# of a string within another string and either returns the position of the string or -1
# if the string was not found, we can write the following loop to show lines which
# contain the string “@uct.ac.za”

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)

# Here we use the contracted form of the if statement where we put the
# continue on the same line as the if. This contracted form of the if functions the
# same as if the continue were on the next line and indented.
