programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])
# An error in a program that prevents the program from running as expected.

programming_dictionary["Dictionary"] = "A mutable, unordered, key-indexed data structure that stores key-value pairs."
# Adding a key to the dictionary

print(programming_dictionary)
# {'Bug': 'An error in a program that prevents the program from running as expected.', 
# 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 
# 'The action of doing something over and over again.', 
# 'Dictionary': 'A mutable, unordered, key-indexed data structure that stores key-value pairs.'}

empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])