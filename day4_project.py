import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

# print(game_images[user]) --second method to print user images but it will also required if else to check out of range value.

if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissors)
else:
    print("\nYou have entered Invalid value.\nPlease try again.")
    exit()
    
game_length=len(game_images)
user_choice=random.randint(0,game_length-1)
comp=game_images[user_choice]
print(f"\nComputer Chose:        {comp}")

if user_choice==user:
    print("Draw.")
elif (user==0 and user_choice==2) or (user==1 and user_choice==0) or (user==2 and user_choice==1):
    print("You Win.")
else:
    print("You Lose.")