# # We really do not want to have to edit our Python code every time we want to
# # process a different file. It would be more usable to ask the user to enter the file
# # name string each time the program runs so they can use our program on different
# # files without changing the Python code.

# This is quite simple to do by reading the file name from the user using input as
# follows:

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Same as above but with try and Except
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# count = 0
# for i in fhand:
#     if i.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)