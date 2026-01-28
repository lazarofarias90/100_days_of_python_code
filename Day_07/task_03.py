import random

# TODO-1: Use a while loop to allow the user to guess again. The game should only stop when the user fills all the spaces in the display (i.e., there are no more underscores in the list).

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []

number_letters = len(chosen_word)
print(number_letters)

for blank in range(0, number_letters):
    display.append("_")

print(display) 

while "_" in display:
    
    guess = input("Choose a letter! ").lower()

    for blank in range(0, number_letters):
        if guess in chosen_word[blank]:
            display[blank] = guess
    print(display)

