# The ssl (secure sockets layer) library allows programs to access web sites that strictly 
# enforce HTTPS. We can apply it in 12.7 program to be able to input other urls. 

# https://docs.python.org/3/library/ssl.html
# https://docs.python.org/3/library/urllib.request.html

# By default urllib.urlopen() has None for certificate argument

import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()      # creates context object to use as the cert argument in urlib.request()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="http[s]?://.+?"', html)
for link in links:
    print(link.decode())