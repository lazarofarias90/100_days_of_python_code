print("Welcome to Python Pizza Deliveries!")
size = input("What pizza size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    print("You chose Small pizza.")
    bill += 15
elif size == "M":
    print("You chose Medium pizza.")
    bill += 20
elif size == "L":
    print("You chose Large pizza.")
    bill += 25
else:
    print("You chose the wrong letter.")

if pepperoni == "Y":
    if size == "s":
        print("You wanted to add pepperoni.")
        bill += 2
    else:
        print("You wanted to add pepperoni.")
        bill += 3

if extra_cheese == "Y":
    print("You wanted to add extra cheese.")
    bill += 1

print(f"Your final bill is: ${bill}")