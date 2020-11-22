# Project Rock Paper Scissors
# How to play the game? https://www.wrpsa.com/
# Starting code - https://repl.it/@appbrewery/rock-paper-scissors-start#main.py


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
computer_random_number = random.randint(0, 2)
game_images = [rock, paper, scissors]
computer_and_user_choices = ["rock", "paper", "scissors"]
input_user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) - 1
computer_choice = computer_and_user_choices[computer_random_number]
user_choice = computer_and_user_choices[input_user_choice]
print(game_images[input_user_choice])
print("Computer chose:")
print(game_images[computer_random_number])
if input_user_choice == 0 and computer_random_number == 0:
    print("It's a DRAW!")
elif input_user_choice == 0 and computer_random_number == 1:
    print("Computer WON!")
elif input_user_choice == 0 and computer_random_number == 2:
    print("You WON!")
elif input_user_choice == 1 and computer_random_number == 0:
    print("You WON!")
elif input_user_choice == 1 and computer_random_number == 1:
    print("It's a DRAW!")
elif input_user_choice == 1 and computer_random_number == 2:
    print("Computer WON!")
elif input_user_choice == 2 and computer_random_number == 0:
    print("You WON!")
elif input_user_choice == 2 and computer_random_number == 1:
    print("Computer WON!")
elif input_user_choice == 2 and computer_random_number == 2:
    print("It's a DRAW!")
