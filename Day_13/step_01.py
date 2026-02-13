def my_function():
    for i in range(1,20):
        if i == 20:
            print("You got it")

my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# The for loop is iterating through the counter i from 1 to 20. However, i does not count 20.
# 2. When is the function meant to print "You got it?"
# When i reaches 20.
# What are your assumptions about the value of i?
# The counter "i" will iterate through the values ​​from 1 to 19, but not 20. 
# That's why the message doesn't appear on the screen.

# The correct code:

def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")

my_function()