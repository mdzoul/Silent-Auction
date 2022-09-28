from replit import clear
from art import *
import time

def find_highest_bid():
    text_logo()

    # To add suspense
    print("Picking highest bid")
    time.sleep(.5)
    print("Picking highest bid.")
    time.sleep(.5)
    print("Picking highest bid..")
    time.sleep(.5)
    print("Picking highest bid...")
    time.sleep(.5)
    clear()

    text_logo()
    highest_bidder = max(name_bid, key=name_bid.get)
    highest_amount = name_bid[highest_bidder]
    print(f"""Congratulations \33[1;32m{highest_bidder}\33[0m!
    
You are the highest bidder with \33[1m{highest_amount} {bid_value}\33[0m.
    
Please make your payment and collect your \33[1m{auction_item}\33[0m.
---""")

end_auction = False
while not end_auction:
    text_logo()
    print("\33[4;32mWelcome to the silent auction program\33[0m\n")
    
    # Choose item to bid on and the currency to bid with
    auction_item = input("What are you bidding on? ")
    bid_value = input("With what are you bidding? ")
    if bid_value == "money":
        bid_value = "dollars"
    clear()
        
    #Adding players and bids
    auction = True
    name_bid = {}
    while auction == True:
        text_logo()
        
        name = input("What is your name? ").capitalize()
        bid = int(input("What is your bid? "))
        name_bid[name] = bid
        
        add_player = input("\nDo you want to add player? Y/N ").lower()
        wrong_input = False
        if add_player == "y":
            auction = True
            clear()
        elif add_player == "n":
            auction = False
            clear()
            find_highest_bid()
        else:
            print("\33[31m[Invaild input]\33[0m")
        
    # If there is another bid
    cont_bid = input("Bid another item? Y/N ").lower()
    if cont_bid == "y":
        end_auction = False
        clear()
    elif cont_bid == "n":
        end_auction = True
        clear()
        text_logo()
        print("\33[31m---Silent auction ended---\33[0m")
        