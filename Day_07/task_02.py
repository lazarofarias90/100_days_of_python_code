import random

# TODO-1: Create an empty list called display. For each letter in chosen_word, add an underscore (_) to the list. (If the word is "camel", the display should be ["_", "_", "_", "_", "_"]).

# TODO-2: Iterate through each position in chosen_word. If the letter in that position matches the guess, replace the underscore (_) in the display at that position with the letter.

# TODO-3: Print the display to see the correct letters and remaining spaces.

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Choose a letter! ").lower()
display = []
number_letters = len(chosen_word)

print(number_letters)

for blank in range(0, number_letters):
    if guess in chosen_word[blank]:
        display.append(guess)
    else:
        display.append("_")

print(display) 