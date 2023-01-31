# Exercise 3: Sometimes when programmers get bored or want to have a
# bit of fun, they add a harmless Easter Egg to their program. Modify
# the program that prompts the user for the file name so that it prints a
# funny message when an easter egg is activated

try:
    file = input('State name: ')
    fileOpen = open(file)

except:
    input('What is your quest?\n')
    reply = input('What is the average airspeed velocity of an unladen swallow?\n')
    reply.lower()
    if reply.find('african') == 1:
        print('...\n...\nHuh, I dont know that!\n....\n...')
        print('WaaaaaaAAAAAAAAAAAAAaaaaaaaaaH')
    elif reply.find('24') == 1 or reply.find('11') == 1: 
        print('Right, off you go.')
    else:
        print('WaaaaaaAAAAAAAAAAAAAaaaaaaaaHa')
    exit()


count = 0

for line in fileOpen:
    count = count + 1
print('There are', count, 'subject lines in', file)