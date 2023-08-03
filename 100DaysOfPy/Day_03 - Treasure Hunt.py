# TITLE: Treasure Hunt Game
# DESCRIPTION: Text-based adventure game
# DATE: 31Jan2023
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
while True:
    choice1 = input("You\'re at a crossroad, which way do you want to go? Left or right?").lower()
    if choice1.count('left'):
        choice2 = input('You find yourself staring before a body of water. Would you like to wait or do something else?').lower()
        if choice2.count('wait'):
            choice3 = input('Amazingly a castle begins to rise from the waters. Before you now stands 3 doors: Red, Blue, and Yellow. What do you want to do next?').lower()
            if choice3.count('red'):
                print("As you enter the red door, fire begins to exhume the room and you burn to death.\nGame Over")
                break
            if choice3.count('blue'):
                print("Creeping into the blue door, you begin to hear growls and screeches from monstrous beasts. They soon maul you to death.\nGame Over")
                break
            if choice3.count('yellow'):
                print('Opening the yellow door, light begins to glisten from inside. The room is filled with treasure.\n You Win!')
                break
            print('Before you could do so, the castle senses a disturbance from your very soul. As it has risen from the waters, it now descends back into it. You have lost the treasure...\nGame Over!')     
        if choice2.count('swim'):
            print('As you you traverse the body of water, using every ounce of strength to swim, trout begins to surround and attack you. You drown to death.\Game Over!')
            break
        print("As you do, other treasure hunters hear the commotion. They find and capture you.\nGame Over.")
        break
    print("You fall into a trap hole.\nGameOver, try again.")
    break