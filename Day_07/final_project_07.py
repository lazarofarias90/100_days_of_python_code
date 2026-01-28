import random
import hangman_art
import hangman_words

# TODO-1: Import the word list from an external file (hangman_words.py).

# TODO-2: Import the game logo from the hangman_art.py file and print it at the beginning.

# TODO-3: If the user types a letter they already guessed, warn them and don't deduct a life.

# TODO-4: At the end, check if the user won (no more underscores) or lost (lives == 0) and show the correct word.

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
number_letters = len(chosen_word)
display = []
used_letters = []
lives = 6

for blank in range(0, number_letters):
    display.append("_")

while "_" in display and lives > 0:
    
    guess = input("Choose a letter! ").lower()

    if guess in used_letters:
        print(f"You've already guessed {guess}. Try another one!")
        continue

    used_letters.append(guess)

    if guess in chosen_word:
        for index in range(number_letters):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        lives = lives - 1

    print(hangman_art.stages[lives])
    print(f"{' '.join(display)}")
    print(f"Lives: {lives}")

if not "_" in display and lives > 0:
    print("You win!")
else:
    print(f"You lost! The correct answer was: {chosen_word}")