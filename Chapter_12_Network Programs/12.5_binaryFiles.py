# Sometimes you want to retrieve a non-text (or binary) file such as an image or
# video file. The data in these files is generally not useful to print out, but you can
# easily make a copy of a URL to a local file on your hard disk using urllib.

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
print(type(img))

img = img.read()
print(type(img))

fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()

# Reads all of the data in at once across the network and stores it in the
# variable img in the main memory of your computer, then opens the file cover.jpg
# and writes the data out to your disk.

# If the file is too large, the program may crash or 
# run extremely slowly when the computer runs out of memory. 
# To solve this, retrieve the data in blocks (or buffers) and then write
# each block to the computer disk before retrieving the next block:

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0

while True:
    info = img.read(512000) # 2 kilobytes
    if len(info) < 1: break
    size = size + len(info) # counter to track amount of characters
    fhand.write(info)
print(size, 'characters copied.')
fhand.close()


