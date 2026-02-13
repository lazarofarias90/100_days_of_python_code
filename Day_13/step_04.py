# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}")

# We have two problems in this code: the first is the incorrect indentation within the if statement. 
# And the second error is the possibility of the user entering strings instead of integers.
# The third part of the bug is realizing that the program doesn't do what you expected it to do.

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You entered an invalid number. Try again with a numerical answer, such as 15.")

apropriate_age = 18

if age > 18:
    print("You can Drive!")
else:
    print(f"You can drive at age {apropriate_age}")
