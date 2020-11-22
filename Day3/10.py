# Project - Treasure Island
# Starting Code - https://repl.it/@appbrewery/treasure-island-start
# Flow Chart - https://bit.ly/36ZQ2av
# Ascii chart for art - https://ascii.co.uk/art

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
left_or_right = (input(
    "You're at a cross road, where do you want to go? Type \"left\" or \"right\".\n").lower())
if left_or_right != "left" or left_or_right == "right":
    print("You fell into a hole, GAME OVER!")
elif left_or_right == "left":
    swim_or_wait = (input(
        "You've come to a lake. There is an island in the middle of the lake.\
Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")).lower()
    if swim_or_wait == "swim" or swim_or_wait != "wait":
        print("You get attacked by an angry trout. GAME OVER!")
    elif swim_or_wait == "wait":
        house_color = (input(
            "You arrive at the island unharmed. There is a house with 3 doors. \
One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose?\n")).lower()
        if house_color == "red":
            print("It's a room full of fire. GAME OVER!")
        elif house_color == "yellow":
            print("You found the treasure, YOU WIN!")
        elif house_color == "blue":
            print("You entered a house full of beasts. GAME OVER!")
        else:
            print("You chose a room that doesn't exist. GAME OVER!")
            