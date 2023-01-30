# Exercise 4: Change the urllinks.py program to extract and count 
# paragraph <p> tags from the retrieved HTML document and display the
# count of the paragraphs as the output of your program. Do not display
# the paragraph text, only count them. Test your program on several
# small web pages as well as some larger web pages.

import urllib.request
import bs4

openUrl = 'https://www.wikipedia.org/wiki/HTML'

myUrl = urllib.request.urlopen(openUrl)
soup = bs4.BeautifulSoup(myUrl,'html.parser')

tags = soup('p')
count = 0

for tag in tags:
    count +=1

print('Number of paragraphs:', count)
#print(soup)
