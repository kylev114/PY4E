# When we want to read or write a file (say on your hard drive), we first must
# open the file.In this example, we open the file mbox.txt, which should be stored in the same
# folder that you are in when you start Python. You can download this file from
# http://www.py4e.com/code3/mbox.txt
# https://www.py4e.com/code3/mbox-short.txt

fhand = open('mbox.txt')
print(fhand)

# If the open is successful, the operating system returns us a file handle. The file
# handle is not the actual data contained in the file, but instead it is a “handle” that
# we can use to read the data. You are given a handle if the requested file exists and
# you have the proper permissions to read the file.
