import random

print("Welcome to the heads or tails game.")
player_choice = input('Make your choice: "Heads" or "Tails". ').lower()

random_result = random.randint(0, 1)

if random_result == 0:
    print('The result was "Heads".')
    if player_choice == "heads":
        print("You Win!")
    elif player_choice == "tails":
        print("You Lose!")
    else:
        print("You made the wrong choice.")
else:
    print('The result was "Tails".')
    if player_choice == "tails":
        print("You Win!")
    elif player_choice == "heads":
        print("You Lose!")
    else:
        print("You made the wrong choice.")