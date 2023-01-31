# Exercise 5: Change the socket program 12.2 so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.

import socket
import re
import time

openSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#openUrl = input('Enter url:')
openUrl = 'http://data.pr4e.org/romeo.txt'
hostUrl = re.findall('http[s]?://([A-z0-9\.]+)',openUrl)
openSocket.connect((hostUrl[0], 80))
cmd = ('GET '+ openUrl + ' HTTP/1.0\r\n\r\n').encode()
openSocket.send(cmd)

data = b''

while True:
    recvData = openSocket.recv(512)
    time.sleep(0.25)
    if len(recvData)<1: break
    data = data + recvData

pos1 = data.find(b'\r\n\r\n')
data = data[pos1+4:]
print(data.decode(), end='')
