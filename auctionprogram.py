logo = """
                         ___________
                         \        /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\ 
                      """
                      
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner =  bidder
            
    print(f"the winner is {winner} with a bid of ${highest_bid}")
    
auction  = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    auction[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(auction)
    elif should_continue == "yes":
        print("\n"*100)