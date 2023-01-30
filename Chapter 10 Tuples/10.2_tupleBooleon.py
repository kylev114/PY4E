# The comparison operators work with tuples and other sequences. 
# Python starts by comparing the first element from each sequence. If they are equal, it goes on to the
# next element, and so on, until it finds elements that differ. Subsequent elements
# are not considered (even if they are really big).

print ((0, 1, 2) < (0, 3, 4))

print((0, 1, 2000000) < (0, 3, 4))

# The sort function works the same way. It sorts the first element, but in
# the case of a tie, it sorts by second element, and so on.
# This feature lends itself to a pattern called DSU (see 10.0)

# Suppose you have a list of words and you want to sort them from
# longest to shortest:

txt = 'I did not know this would be on the quiz!'

words = txt.split()
t = list()

for word in words:                  # builds a list of tuples, where each tuple is a word preceded by its length.
    t.append((len(word), word))
    #print(t)

t.sort(reverse=True)                # compares the first element, length, first, and only considers the second element to break ties.
                                    # sorts by length, then by reverse alphabetical order
answer = list()

for length, word in t:              # traverses the list of tuples and builds a list of words in descending order of length
    answer.append(word)
    
print(answer)
