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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
first_choice = input("Type 'left' or 'right' ").lower()
if first_choice == "left":
    print("You arrive at a lake with an island in the middle of it.")
    second_choice = input("Do you 'wait' for a boat to arrive or do you 'swim' across the lake? ").lower()
    if second_choice == "wait":
        print("After a while, a boat appears out of nowhere and takes you to the island.")
        print("Upon arriving on the island, you will see three doors: a red one on the left, a yellow one in the middle, and a blue one on the right.")
        third_choice = input("Do you choose 'red', 'yellow', or 'blue'?").lower()
        if third_choice == "yellow":
            print("You Win!")
        elif third_choice == "red":
            print("Burned by fire. Game Over!")
        elif third_choice == "blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("You chose the wrong option. Game Over!")
    else:
        print("Attacked by trout. Game Over!")
else:
    print("Fall into a hole. Game Over!")