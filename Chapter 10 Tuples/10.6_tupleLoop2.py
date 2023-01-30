# Augment 9.4 to count the ten most common words from the file
# romeo-full.txt and print them out in the text as follows:

    # 61 i
    # 42 and
    # 40 romeo
    # ...
    # 24 thee

import string 

fhand = open('romeo-full.txt') 

counts = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1 
#print(counts)

topTen = []

for (key,val) in list(counts.items()):
    topTen.append((val,key))               
topTen.sort(reverse=True)

for (key,val) in topTen[:10]:
    print(key,val)

# Note line 30 where key, val is switched in order. 
# When sort method applies, it sorts first parameter (key) which is str before second parameter (val) which is int.
# Reversing it allows the int parameter to be sorted to find top ten most common words.