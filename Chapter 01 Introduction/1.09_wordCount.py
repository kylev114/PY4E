#Sample chapter 10 script
#Recieves input file and outputs frequent word and its total count
#Search for input file within same folder as this script: 
#C:/Users/kaivo/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/kaivo/py4e Notes/1.9_wordCount.py"

name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
