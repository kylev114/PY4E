# One simple way to parse HTML is to use regular expressions to repeatedly search
# for and extract substrings that match a particular pattern.

# Here is a simple web page in html:
#     <h1>The First Page</h1>
#     <p>
#     If you like, you can switch to the
#     <a href="http://www.dr-chuck.com/page2.htm">
#     Second Page</a>.
#     </p

# The url link values can be located using the href attribute
# and applying it onto a regex:

urlRegex = 'href="http[s]?://.+?"'

# The 2nd question mark is to be “non-greedy” to find 
# the smallest possible matching string instead of “greedy” 
# which tries to find largest possible matching string.

# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re

url = 'https://docs.python.org'
html = urllib.request.urlopen(url)

html = html.read()
links = re.findall(urlRegex.encode(), html)
for link in links:
    print(link.decode())

# The read method returns HTML source code as a bytes object instead of an HTTPResponse object.
# The findall regular expression method returns a list of all of the strings that match regex. 
# Note that the regex must be encoded in bytes becuse the html is a byte object.
# The for loop help seprate each link (elements) of links (list) to be printed.

