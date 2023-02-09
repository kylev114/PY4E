# Refer to functions (chapter 4). At its most basic, functions 
# takes inputs and returns outputs. The input/output are on the
# "outside" which is seperated from the function code "inside."

# Refer to BeautifulSoup program (12.8) and (14.4) figure.
# This program takes a url input and outputs the href tags. 
# Within the program are several processes:

    # URL is read into a string and then passed into urllib to retrieve the data
    # from the web. The urllib library uses the socket library to make the actual
    # network connection to retrieve the data. Urllib returns a string which is passed
    # to BeautifulSoup for parsing. BeautifulSoup makes use of the object
    # html.parser1 and returns an object. tags() method is called on the returned
    # object that returns a dictionary of tag objects. Thet tags are looped through  
    # the get() method is called for each tag to print out the href attribute.

# This movement of interacting objects and infomration is contained 
# within the program, like the black box of a function. 

# With O-OP, complex systems can be broken into parts. The parts of 
# BeautifulSoup library is ignored and using the program only 
# requires knowledge about the string object inputs and outputs.

# The creators of BeautifulSoup library did not create their library
# to ensure programmers can create a href parser. They created the object
# that can be incorporated into programs like 12.8 without requiring
# the resources and time to understand what is happening on the "inside"
# of their program. 