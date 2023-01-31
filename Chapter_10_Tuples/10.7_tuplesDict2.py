# Because tuples are hashable and lists are not, if we want to create a composite key
# to use in a dictionary we must use a tuple as the key.
# I.e. use a tuple to create a name tuple:

directory = {('Python','Monty'):42}


for (lastName,firstName) in directory:
    print(firstName, lastName, directory[lastName,firstName])

