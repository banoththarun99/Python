def find_heighest_bidder(bidding_dictionary):
    winner = ""
    heighest_bid = 0
    
    for bidder in bidding_dictionary:
        bidder_amount = bidding_dictionary[bidder]
        
        if bidder_amount > heighest_bid:
            heighest_bid = bidder_amount
            winner = bidder
            
    print(f"the winner is {winner} with the bid of ${heighest_bid}.")
    
bids = {}
continue_bidding = True
while continue_bidding :
    name = input("what is your name : ")
    price = int(input("what is your bid price? : $"))
    bids[name] = price
    should_continue = input("are anyone ready to bid? type 'yes' or 'no' \n").lower()
    
    if should_continue == "no":
        continue_bidding = False
        find_heighest_bidder(bids)
        
    elif should_continue == "yes":
        print("\n" * 40)
        
    else :
        print("no bidding cancle the Action")