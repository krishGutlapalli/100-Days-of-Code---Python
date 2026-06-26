print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your at a crossroad.")
crossroad = input("Do you want to go right or left?")
if crossroad == "right" or crossroad == "Right" or crossroad == "r" or crossroad == "R":
    print("You have fell into a hole. Game Over, Try Again")
elif crossroad == "left" or crossroad == "Left" or crossroad == "l" or crossroad == "L":
    print("You've come to a lake. There is a island in the middle of the lake.")
    lake = input("do you want to wait for a boat or swim across?")
    if lake == "swim" or lake == "Swim" or lake == "S" or lake == "s" or lake == "Swim across" or lake == "swim across":
        print("You get attacked by trout. Game Over, Try Again")
    elif lake == "wait" or lake == "Wait" or lake == "W" or lake == "w" or lake == "Wait for boat" or lake == "wait for boat":
        print("You have arrived at the island unharmed. There is a house with 3 doors.")
        door = input("There is a red door, a blue door, and a yellow door. Which do you choose?")
        if door == ("red" or door == "Red" or door == "R" or door == "r" or door == "red door" or door == "Red door"):
            print("You get burned by fire. Game Over, Try Again")
        elif door == ("blue" or door == "Blue" or door == "B" or door == "b" or door == "blue door" or door == "Blue door"):
            print("You get eaten by beasts. Game Over, Try Again")
        elif door == ("yellow" or door == "Yellow" or door == "Y" or door == "y" or door == "yellow door" or door == "Yellow door"):
            print("You Win!!!")