# Exercise 1: Change the socket program 12.2 to prompt the user
# for the URL so it can read any web page. You can use split('/') to
# break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an improperly
# formatted or non-existent URL.

# Remember socket.connect must be with the host domain and the GET command is 
# attached to the specific url within the host domain. 

import socket
import re

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    openUrl = 'http://data.pr4e.org/romeo.txt'
    # openUrl = input("Enter url:")
    hostUrl = re.findall('http[s]?://([A-z0-9\.]+)',openUrl)
    mySock.connect((hostUrl[0], 80)) # index because the re.findall() method returns a list
    cmd = ('GET '+ openUrl + ' HTTP/1.0\r\n\r\n').encode()
    mySock.send(cmd)
   
except:
    print('Invalid url')
    exit()

while True:
    data = mySock.recv(512)
    if len(data) < 1: break
    print(data.decode(), end='')
mySock.close()