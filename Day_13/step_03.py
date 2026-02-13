# year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# If you choose 1994, nothing happens. 
# So you have to think like the computer thinks in order to find the solution to the problem.

year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

