# While we can manually send and receive data over HTTP using the socket library,
# there is a much simpler way to perform this common task in Python by using the
# urllib library.

# Using urllib, you can treat a web page much like a file. You simply indicate
# which web page you would like to retrieve and urllib handles all of the HTTP
# protocol and header details. The following is equivalent to 12.2:

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# As an example, we can write a program to retrieve the data for romeo.txt and
# compute the frequency of each word in the file as follows:

fileOpen = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fileOpen:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# Refer to urllib documentation for more functionality:
# https://docs.python.org/3/library/urllib.html