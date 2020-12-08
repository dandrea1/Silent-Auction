from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
bid_dictionary = {}
bidding_finished = False
print(art.logo)
print("Welcome to the Silent Auction")

def add_bidder_to_dictionary(bidder_name,bidder_bid):
    bid_dictionary[bidder_name] = bidder_bid

def find_highest_bidder(bidding_record):
    max_bid = 0.00
    winner = ""
    for bidder in bid_dictionary:
        bid_as_float = bid_dictionary[bidder]
        if bid_as_float > max_bid:
            max_bid = bid_as_float
            winner = bidder
    print(f"Congratulations, {winner}, you win with a bid of ${max_bid}")

while bidding_finished == False:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    add_bidder_to_dictionary(bidder_name = name,bidder_bid = bid)
    should_continue = input("Is there another bidder? Type yes or no.\n").lower()
    if should_continue == 'no':
        bidding_finished = True
        clear()
    elif should_continue == 'yes':
        clear()

find_highest_bidder(bid_dictionary)
