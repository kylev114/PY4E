# Usually when we are reading a file we want to do something to the lines other than
# just printing the whole line. Often we want to find the “interesting lines” and then
# parse the line to find some interesting part of the line. What if we wanted to print
# out the third word, which is the day, from those lines that start with “From”?

# "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

fhand = open('mbox-short.txt')
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
