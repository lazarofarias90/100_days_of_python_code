print("Welcome to the game of numbers.")
print("Tell me a number and I'll tell you if it's even or odd.")

chosen_number = int(input("Your number is "))
two_rest = chosen_number % 2

if two_rest == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")