import os

def clear():
    os.system('clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        # Convert string to int to allow comparison
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = input("What is your bid?: $")
    bids[name] = price
    
    # Validation loop for the answer
    valid_answer = False
    while not valid_answer:
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        
        if should_continue == "no":
            valid_answer = True
            bidding_finished = True
            clear()
            find_highest_bidder(bids)
        elif should_continue == "yes":
            valid_answer = True
            clear()
        else:
            print("Invalid input! Please type 'yes' or 'no'.")