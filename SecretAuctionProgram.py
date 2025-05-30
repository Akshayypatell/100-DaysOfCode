other_bidders = True
import os
information = {}
while other_bidders:
    name = input("What is your name?: ")
    bid = input("Whats your bid?: $")
    information[name] = bid
    bidder = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if bidder == "yes":
        other_bidders = True
        print("\n"*100)
    elif bidder == "no":
        other_bidders = False

max_value = max(information, key=information.get)

print(f"The winner is {max_value} with a bid of ${information[max_value]}")
