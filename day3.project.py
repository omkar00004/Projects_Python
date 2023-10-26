# Code for treasure island - Story game
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

step1=input("In which direction you want to, Left to cross across junglee and right to cross acore snow mountain and terrain.")

lower_step1=step1.lower()

if lower_step1=="left":
    print("Turns out Junglee is safer, you can pass through it easily")
elif lower_step1=="right":
    print("Game over\nTurns out Mountain is a bad dicision, You became a meal of snow leopard")
    quit()
else:
    print("You type unappropriate words,Please try again.")
    
step2=input("\nTo get to the treasure, what next step you want to take...\nTo swim across the lake or wait for boat.")

lower_step2=step2.lower()

if lower_step2=="wait":
    print("You made a right decision, the lake is full of crocodile and pirrana's")
elif lower_step2=="swim":
    print("You made a bad dicision, the  lake is full of crocodile and pirrana's \nGame over\nBetter luck next time" )
    quit()
else:
    print("You type unappropriate words,Please try again.")
    
step3=input("\nWell done, you made to the end, one last step and tresure is yours...\nThere are three door - Red, Yellow, Blue and behind one doors is treausre.\nBe carful other doors are dangerous.")

lower_step3=step3.lower()

if lower_step3=="yellow":
    print("\nYou won the game...\nThe treasure is all yours.")
elif lower_step3=="blue":
    print("Killed by beasts and treasure hunter\nGame over")
    quit()
elif lower_step3=="red":
    print("Burned by fire\nGame over")
    quit()
else:
    print("You type unappropriate words,Please try again.")
    