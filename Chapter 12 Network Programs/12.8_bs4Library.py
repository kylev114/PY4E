# There are a number of Python libraries which can help you parse HTML and
# extract data from the pages. Each of the libraries has its strengths and weaknesses
# and you can pick one based on your needs.

# As an example, we will simply parse some HTML input and extract links using
# the BeautifulSoup library. BeautifulSoup tolerates highly flawed HTML and still
# lets you easily extract the data you need.

# https://pypi.org/project/beautifulsoup4/ 
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# We will use urllib to read the page and then use BeautifulSoup to extract the
# href attributes from the anchor <a> tags:

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://docs.python.org'
openHtml = urllib.request.urlopen(url, context=ctx).read()

#converts html data (bytes object) to bs4.BeautifulSoup object
soup = BeautifulSoup(openHtml, 'html.parser') 

# stores all of html data with <a> tag as a bs4.element object 
tags = soup('a') 

# extracts attributes from all the <a> tags of the html file
for tag in tags:                          
    #print('URL:', tag.get('href', None))  
    print('TAG:', tag)
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)


