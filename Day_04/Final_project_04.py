import random

print('Welcome to the "Rock, Paper, Scissors" game.')
print("What do you chose?")
player_choice = int(input("Type 0 for Rock, 1 for Paper o 2 for Scissors: "))
computer_choice = random.randint(0, 2)

if player_choice == 0:
    print("Your chose:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    if computer_choice == 0:
        print("The computer chose:")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("Nobody won!")
    elif computer_choice == 1:
        print("The computer chose:")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You lose!")
    else:
        print("The computer chose:")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You win!")

if player_choice == 1:
    print("Your chose:")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    if computer_choice == 0:
        print("The computer chose:")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You win!")
    elif computer_choice == 1:
        print("The computer chose:")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("Nobody won!")
    else:
        print("The computer chose:")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You lose!")

if player_choice == 2:
    print("Your chose:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if computer_choice == 0:
        print("The computer chose:")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You lose!")
    elif computer_choice == 1:
        print("The computer chose:")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You win!")
    else:
        print("The computer chose:")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("Nobody won!")

else:
    print("You chose the wrong number!")
