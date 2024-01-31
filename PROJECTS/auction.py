import os
from time import sleep

bidders_list = []
bidder_name = input("What is your name: ")
bids = int(input("Whats your bid: $"))

bidding_cont = True

def new_dic():
    bid_log = {}
    bid_log[bidder_name] = bids
    bidders_list.append(bid_log)
    return bid_log

def highest_bidder(record):
    highest_bidder = 0
    for key, value in record.items():
        if value > highest_bidder:
            highest_bidder = value
    print(f"highest bidder is {key} amount ${highest_bidder}")


while bidding_cont:
    log_new = new_dic()
    print("New bidder...?")
    question = input("Continue bidding? yes/no: ").lower()
    
    if question in ['no', "n"]:
        bidding_cont = False
        highest_bidder(log_new)
    elif question in ['yes', 'y']:
        os.system('clear')
        bidder_name = input("What is your name: ")
        bids = int(input("Whats your bid: "))
