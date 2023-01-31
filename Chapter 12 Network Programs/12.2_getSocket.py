# Refer to page 36 of HTTP to find the syntax for the GET request. 
# To request a document from a web server, we make a connection to 
# the www.pr4e.org server on port 80, and then send a line of the form

# GET http://data.pr4e.org/romeo.txt HTTP/1.0

# where the second parameter is the web page we are requesting, and then we also
# send a blank line. The web server will respond with some header information about
# the document and a blank line followed by the document content.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Sets family and type of socket made, refer to socket documentation for more info
mysock.connect(('data.pr4e.org', 80)) # Note how argument is a tuple (double parenthesis)                   
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

# Lines 13-16
# First the program declares a new socket using the .socket() function; note the function parameters 
# defines the address family and socket type. (Refer to python socket documentation). 
# Then it makes a connection to port 80 on the server 'www.py4e.com'.
# (Port 80 is the default network port used to send and receive unencrypted web pages per HTTP.)
# Since our program is playing the role of the “web browser”, the HTTP 
# says we must send the GET command followed by a blank line. \r\n signifies
# an EOL (end of line), so \r\n\r\n signifies nothing between two EOL sequences.
# That is the equivalent of a blank line. 
# The GET command is sent using the .send() function which sends it through the socket.

# Lines 18-23
# Once we send that blank line, we write a loop that uses .recv() function to 
# receives data. 512 is the bufsize meaning we recieve 512 characters at a time 
# (equivalent to 2 bytes). The socket will now continously send data to be recieved 
# from our socket until there is nothing left. The loop  will print the data out 
# until there is no more data to read (i.e., the .recv() returns an empty string).

# Line 15, 22
# Note .encode() and .decode() methods. HTTP requires data sent and recieved to be byte objects.
# b'' is equivalent to encode(); (i.e. encode('hello world') = b'hello world') 

# Data Recieved
# The output starts with headers which the web server sends to describe the document. 
# For example, the Content-Type header indicates that the document is a
# plain text document (text/plain).After the server sends us the headers, 
# it adds a blank line to indicate the end of the headers, 
# and then sends the actual data of the file romeo.txt.

