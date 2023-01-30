# A text file can be thought of as a sequence of lines, much like a Python string can
# be thought of as a sequence of characters. For example, this is a sample of a text
# file which records mail activity from various individuals in an open source project
# development team:


# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Return-Path: <postmaster@collab.sakaiproject.org>
# Date: Sat, 5 Jan 2008 09:12:18 -0500
# To: source@collab.sakaiproject.org
# From: stephen.marquard@uct.ac.za
# Subject: [sakai] svn commit: r39772 - content/branches/
# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
# ...


# The entire file of mail interactions is available from
# www.py4e.com/code3/mbox.txt
# and a shortened version of the file is available from
# www.py4e.com/code3/mbox-short.txt
# These files are in a standard format for a file containing multiple mail messages.
# The lines which start with “From” separate the messages and the lines which start
# with “From:” are part of the messages. For more information about the mbox
# format, see https://en.wikipedia.org/wiki/Mbox.

# To break the file into lines, there is a special character that represents the “end of
# the line” called the newline character

# In Python, we represent the newline character as '\n' in string constants.
# Even though this looks like two characters, it is actually a single character. When
# we look at the variable by entering “stuff” in the interpreter, it shows us the \n
# in the string, but when we use print to show the string, we see the string broken
# into two lines by the newline character

print('Hello\nWorld!')
print('X\nY')

# So when we look at the lines in a file, we need to recognize that there is a special
# invisible character called the newline at the end of each line that marks the end of
# the line