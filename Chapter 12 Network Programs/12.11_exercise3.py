# Exercise 3: Use urllib to replicate 12.11.2 of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

import urllib.request
from urllib.parse import urlparse
import re
import time

try:
    openUrl = 'https://www.wikipedia.org/wiki/HTML'
    myUrl = urllib.request.urlopen(openUrl)
    hostUrl = urlparse(openUrl)
    
except:
    print('Invalid url')
    exit()

fileList = []

print(myUrl.read(3000).decode()) #includes whitespace
  
print('Host Name:', hostUrl.netloc)
print("File Length:", len(myUrl.read(3000)))


# for line in myUrl:
#      print(line.decode().strip())

#Convert file str into list to limit only first 3001 characters
# for line in myUrl:
#      print(line.decode().strip())
#      for words in line.decode().split():
#         fileList.append(words)
# fileList = fileList[:3001]
# fileStr = ' '.join(fileList)
# print(fileStr)