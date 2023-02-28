# Refer to functions (chapter 4). At its most basic, functions 
# take inputs and return outputs. The input/output are on the
# "outside" which is interactable with the user.
# The function code "inside" entails the actual process behind 
# the prograom and is not easily accessible to the user.

# Refer to BeautifulSoup program (12.8) and (14.4) figure.
# This is a procedural program takes a url input and outputs the href tags. 
# Within the program are several processes:

    # URL is read into a string and then passed into urllib to retrieve the data
    # from the web. The urllib library uses the socket library to make the actual
    # network connection to retrieve the data. Urllib returns a string which is passed
    # to BeautifulSoup for parsing. BeautifulSoup makes use of the object
    # html.parser1 and returns an object. tags() method is called on the returned
    # object that returns a dictionary of tag objects. Thet tags are looped through  
    # the get() method is called for each tag to print out the href attribute.

# This movement of interacting objects and information is contained 
# within the program, and when ignored, is a black box function. 

# With O-OP, complex systems can be broken into parts. The parts of 
# BeautifulSoup library is ignored and using the program only 
# requires knowledge about the string object inputs and outputs.

# The creators of BeautifulSoup library did not create their library
# to ensure programmers can create a href parser. They created the object
# that can be incorporated into programs like 12.8 without requiring
# the resources and time to understand what is happening on the "inside"
# of their program. 

import csv

class Nothing():
    
    @classmethod
    def readCSV(cls):  
        fileOpen = open('items.csv', 'r')
        fileRead = csv.DictReader(fileOpen)
        items = list(fileRead)
                
        for item in items:
                print(item)

Nothing.readCSV()
