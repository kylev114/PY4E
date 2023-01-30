# Exercise 2: Change your socket program 12.11.1 so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire document 
# and count the total number of characters and display the count
# of the number of characters at the end of the document.
# Remember that data stream may be inconsistent due to connection

import socket
import re
import time

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    openUrl = 'http://data.pr4e.org/mbox-short.txt'
    # openUrl = input("Enter url:")
    hostUrl = re.findall('http[s]?://([A-z0-9\.]+)',openUrl)
    mySock.connect((hostUrl[0], 80)) # index because the re.findall() method returns a list
    cmd = ('GET '+ openUrl + ' HTTP/1.0\r\n\r\n').encode()
    mySock.send(cmd)
    
except:
    print('Invalid url')
    exit()

count = 0

while True:
    data = mySock.recv(600)
    if len(data) < 1 or count >= 3000: break
    time.sleep(0.25)    # ensures each data stream is exactly bufsize
    count = count + len(data.decode())
    print((data.decode()), '\nCount:',count)

mySock.close()
