#initial code

"""
from colorama import Fore

print(Fore.YELLOW + "Welcome to Treasure Island, your mission is to find the treasure. Have fun!")

print(Fore.RED + '''
─────────────────────────────────
───────────────▄████████▄────────
─────────────▄█▀▒▒▒▒▒▒▒▀██▄──────
───────────▄█▀▒▒▒▒▒▒▒▒▒▒▒██──────
─────────▄█▀▒▒▒▒▒▒▄▒▒▒▒▒▒▐█▌─────
────────▄█▒▒▒▒▒▒▒▒▀█▒▒▒▒▒▐█▌─────
───────▄█▒▒▒▒▒▒▒▒▒▒▀█▒▒▒▄██──────
──────▄█▒▒▒▒▒▒▒▒▒▒▒▒▀█▒▄█▀█▄─────
─────▄█▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▀▒▒▒█▄────
────▄█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▄───
───▄█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▄──
──▄█▒▒▒▄██████▄▒▒▒▒▄█████▄▒▒▒▒█──
──█▒▒▒█▀░░░░░▀█─▒▒▒█▀░░░░▀█▒▒▒█──
──█▒▒▒█░░▄░░░░▀████▀░░░▄░░█▒▒▒█──
▄███▄▒█▄░▐▀▄░░░░░░░░░▄▀▌░▄█▒▒███▄
█▀░░█▄▒█░▐▐▀▀▄▄▄─▄▄▄▀▀▌▌░█▒▒█░░▀█
█░░░░█▒█░▐▐──▄▄─█─▄▄──▌▌░█▒█░░░░█
█░▄░░█▒█░▐▐▄─▀▀─█─▀▀─▄▌▌░█▒█░░▄░█
█░░█░█▒█░░▌▄█▄▄▀─▀▄▄█▄▐░░█▒█░█░░█
█▄░█████████▀░░▀▄▀░░▀█████████░▄█
─██▀░░▄▀░░▀░░▀▄░░░▄▀░░▀░░▀▄░░▀██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░▄░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░█
█░▀█▄░░░░░░░░░░░░░░░░░░░░░░░▄█▀░█
█░░█▀███████████████████████▀█░░█
█░░█────█───█───█───█───█────█░░█
█░░▀█───█───█───█───█───█───█▀░░█
█░░░▀█▄▄█▄▄▄█▄▄▄█▄▄▄█▄▄▄█▄▄█▀░░░█
▀█░░░█──█───█───█───█───█──█░░░█▀
─▀█░░▀█▄█───█───█───█───█▄█▀░░█▀─
──▀█░░░▀▀█▄▄█───█───█▄▄█▀▀░░░█▀──
───▀█░░░░░▀▀█████████▀▀░░░░░█▀───
────▀█░░░░░▄░░░░░░░░░▄░░░░░█▀────
─────▀██▄░░░▀▀▀▀▀▀▀▀▀░░░▄██▀─────
────────▀██▄▄░░░░░░░▄▄██▀────────
───────────▀▀███████▀▀───────────
''')



left = (Fore.YELLOW + "Do you want to swim through the underground tunnel or wait and look around?\n")
right = (Fore.RED + "You got headshotted by a ratatouille!\n")

swim = (Fore.RED + "You got eaten by a bigass shark!\n")
wait = (Fore.YELLOW + "You arrived to a hall, which door do you pick? Red, Blue or Yellow?!\n")

red = (Fore.YELLOW + "You ended up in a room full of treasure. You win!\n")
blue = (Fore.RED + "You got destroyed by a ratatouille pack!\n")
yellow = (Fore.RED + "You enter the next hall. To be continued..!\n")

left_right = input(Fore.YELLOW + "You enter the dungeon, do you go left or right?\n")
left_right = left_right.lower()
if left_right == "right":
    print(f"{right}")

elif left_right == "left":
    left = input(Fore.YELLOW + "Do you want to swim through the underground tunnel or wait and look around?\n")
    left = left.lower()

if left == "swim":
    print(f"{swim}")

elif left == "wait":
    wait = input(Fore.YELLOW + "You arrived to a hall, which door do you pick? Red, Blue or Yellow?!\n")
    wait = wait.lower()

    if wait == "red":
        print(f"{red}")

    elif wait == "blue":
        print(f"{blue}")

    elif wait == "yellow":
        print(f"{yellow}")

    else:
        print(Fore.RED + "Game over.")
else:
    print(Fore.RED + "Game over.")
"""



#Corrected code

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

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


