# Built-in functions can be used to quickly look through a list 
# without needing to write a loops:

nums = [3, 41, 12, 9, 74, 15]

print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums))

print(sum(nums)/len(nums))

# Note that some functions may work with one class, some classes, or all classes.
# Check documentation to see if the elements in a list will work with a function. 

# In addition, functions can also be an element in a list. The first loop
# adds the function addNum() into the list functList(); note how the function
# object was appended without parenthesis since there is no argument.

functList = []

for i in range(5):
    def addNum(x):
        return x + i
    functList.append(addNum)
print(functList)

# Rememeber in line 28, if we print a function it only tells us the object location
# A second loop can be used to go through the list of functions and pass an argument.

for j in functList:
    print(j(12))
