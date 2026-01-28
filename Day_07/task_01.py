import random

# TODO-1: Create a list of words called word_list. (It starts with "ardvark", "baboon", and "camel").

# TODO-2: Randomly choose a word from word_list and assign it to a variable called Chosen_word.

# TODO-3: Ask the user to guess a letter and assign the answer to a variable called guess. Ensure it is lowercase.

# TODO-4: Verify that the letter the user typed (guess) is one of the letters in Choose_Word.

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Choose a letter! ").lower()
if guess in chosen_word:
    print("Ok!")
else:
    print("You lost a life!")