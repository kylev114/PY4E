# TITLE: Blind Auction
# DESCRIPTION: Creates a blind auction by asking for an input for number of participants and their bids; 
# returns highest bidder and their bid
# DATE: 05Feb2023

import os

auctDict = {}

while True:
    name = input('What is you name?:\n')
    bid = float(input('What is your bid?\n$'))
    bid = float("{:.2f}".format(bid))
    auctDict[name] = bid
    reBid = input("Are there any more bidders? Y or N\n").lower()
    os.system('cls')
    if 'n' in reBid: break 

auctList = list(auctDict.values())
auctList.sort(reverse=True)

print(f'Winning bid is: ${auctList[0]} by\n')

for name,bid in auctDict.items():
        if bid == auctList[0]: print(name)


# Reflection:
# Sorting through a dictionary by value is harder to do efficiently than by keys. Even with tuple loops
