from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False


def highest_bidding(bidding_detail):
    highest_bid = 0
    winner = ""
    for bidder in bidding_detail:
        bid_amount = bidding_detail[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid amount of {highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))
    bids[name] = price
    should_continue = input(
        "Is there any other bidder? Type 'yes' to continue and 'no' to exit "
    ).lower()
    if should_continue == "no":
        bidding_finished = True
        highest_bidding(bids)
    elif should_continue == "yes":
        clear()
