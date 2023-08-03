# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
trueFate = 'true'
loveFate = 'love'

trueCount = 0
loveCount = 0

for letter in name1.lower():
    if trueFate.count(letter):trueCount+=1
    if loveFate.count(letter):loveCount+=1

for letter in name2.lower():
    if trueFate.count(letter):trueCount+=1
    if loveFate.count(letter):loveCount+=1

count = trueCount*10+loveCount

if count>90 or count<10:
    print(f"Your score is {count}, you go together like coke and mentos.")
    exit()
if count >= 40 and count<=50:
    print(f"Your score is {count}, you are alright together.")
    exit()
print(f"Your score is {count}.")

