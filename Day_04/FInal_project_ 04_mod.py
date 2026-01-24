import random

print('Welcome to the "Rock, Paper, Scissors" game.')
print("What do you choose?")

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
---'    ____)____
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

game_images = [rock, paper, scissors]

player_choice = int(input("Type 0 for Rock, 1 for Paper o 2 for Scissors:\n"))
if player_choice >= 0 and player_choice <=2:
    print(game_images[player_choice])

computer_choice = random.randint(0, 2)
print("The computer chose:")
print(game_images[computer_choice])

if player_choice > 2 or player_choice < 0:
    print("You typed an invalid number. You lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice > player_choice:
    print("You lose!")
elif computer_choice == player_choice:
    print("It's a draw!")