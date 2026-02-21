import random
from art import logo, vs
from game_data import data

# 1. Function to format the data (keeps the code clean)
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# 2. Function to check the response
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# --- START OF THE GAME ---
print(logo)
score = 0
game_should_continue = True
account_a = random.choice(data) # Initial choice of A

while game_should_continue:
    account_b = random.choice(data)
    
    # Ensures that B is not equal to A.
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Get the follower count to compare.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        # The "Cat's Leap": B becomes the new A for the next round!
        account_a = account_b
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")