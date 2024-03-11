def find_highest_bidder(bid_list):
	for name in bid_list:
		if bid_list[name] == max(bid_list.values()):
			print(f'{name} won the auction for a price of ${bid_list[name]}')

everyone_who_bid = {}
keep_going = True
while keep_going:
	name = input("What is your name?: ")
	price = float(input("How much $ would you like to bid? $"))
	everyone_who_bid[name] = price
	new_player = input("Are there other people who want to bid? Y/N\n").lower()
	if new_player == 'n':
		keep_going = False
		find_highest_bidder(everyone_who_bid)
