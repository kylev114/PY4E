# Often, we want to look into a string and find a substring. For example if we were
# presented a series of lines formatted as follows:

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# and we wanted to pull out only the second half of the address (uct.ac.za)
# from each line, we can do this by using the find method and string slicing

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

position_1= data.find('@') #finds start of substring
print(position_1)

position_2 = data.find(' ', position_1) #finds end of substring (first space after @)
print(position_2)

address = data[position_1:position_2+1] #selects substring using index
print(address)