import random
import hangman_art

# TODO-1: Create a variable called lives to track the number of lives and set it to 6.

# TODO-2: If the guess is not in the chosen_word, reduce lives by 1. If lives reaches 0, the game ends and you print "You lose".

# TODO-3: Print the ASCII art corresponding to the number of lives remaining (the hangman stages it provides in the hangman_art.py file).

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
lives = 6

number_letters = len(chosen_word)
print(number_letters)

for blank in range(0, number_letters):
    display.append("_")

print(display) 

while "_" in display and lives > 0:
    
    guess = input("Choose a letter! ").lower()

    if guess in chosen_word:
        for index in range(number_letters):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        lives = lives - 1
    print(hangman_art.stages[lives])
    print(display)
    print(lives)