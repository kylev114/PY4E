# In the previous example(12.2), we retrieved a plain text file which had newlines in the file
# and we simply copied the data to the screen as the program ran. We can use a
# similar program to retrieve an image across using HTTP. Instead of copying the
# data to the screen as the program runs, we accumulate the data in a string, trim
# off the headers, and then save the image data to a file as follows:

import socket
import time

HOST = 'data.pr4e.org'
PORT = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data
mysock.close()

# Look for the end of the header removes it from picture (2nd CRLF).
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode()) # Prints header
picture = picture[pos+4:]     # +4 accounts for the blank line; len('\r\n\r\n') = 4

# Creates a new .jpg file to store the picture in.
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

# Lines 20-27; Same loop as 12.2
# The count variable allows us to track running total of data being sent after 
# each .recv() cycle. The len(data) shows total data sent for only the current 
# .recv() cycle (based on bufsize). The data itself is stored in picture. 

# Line 21, 23
# As the program runs, note we we don’t get 5120 characters each time
# we call the recv() method. This is depenedent on network speed. 
# We can use time.sleep() to slow down the .recv() calls so that the server 
# can “get ahead” of us and send more data before we call recv()
# again. With the delay we can get a more consistent data stream. 

# Lines 30-32
# Once the data has been fully stored in picture, we strip the headers.
# We use the same blank line ('\r\n\r\n') which marks the end of the header
# and start of the blank line. We remove both the header and blank line to 
# retain only the pciture data. 

# Line 36
# The argument 'wb' for the open() function to set the mode for writing in binary.
# Note that picture value is till all in binary as it hasn't been through .decode() yet.

# The Content-Type header indicates that body of the document is an image (image/jpeg).
# The image, stuff.jpg, can be seen in the folder directory now. 
# Note that not removing the header data causes the .jpg file to be unreadable
