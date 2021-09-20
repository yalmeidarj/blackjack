############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##########################################
import random
# global end_of_game, is_greater_21 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_score_list = []
def user_get_another_card(cards):
	"""Return a random card value"""
	card = random.choice(cards)
	user_score_list.append(card)
	user_total_score = sum(user_score_list)
	if user_total_score > 21:
		end_of_game = True
		return end_of_game		
	return user_total_score

dealer_score_list = []
def dealer_get_another_card(cards):
	"""Return a random card value"""
	card = random.choice(cards) 
	dealer_score_list.append(card)
	dealer_total_score = sum(dealer_score_list)
	if dealer_total_score > 21:
		end_of_game = True
		return end_of_game
	return dealer_total_score  	 
players = {"user":[user_score_list],
"dealer":[dealer_score_list]
}

def winning_player(n1, n2):
	n1 = user_score_list
	n2 = dealer_score_list
	is_greater_than_21(n1)		
	if sum(n1) > sum(n2):
		if sum(n1) < 21:
			winner = (f" The winner is... YOU. your cards are:{players['user']}, with a total of {sum(user_score_list)}")
			return winner
		else:
			winner = (f" The winner is... The dealer :'( Its cards are: {players['dealer']}, with a total of {sum(dealer_score_list)}")
			return winner
	else:
		winner = (f" The winner is...The dealer :'( Its cards are: {players['dealer']}, with a total of {sum(dealer_score_list)}")
		return winner
	if sum(n1) < sum(n2):
		if sum(n2) <21:
			winner = (f" The winner is...The dealer :'( Its cards are: {players['dealer']}, with a total of {sum(dealer_score_list)}")
			return winner
		else:
			winner = (f" The winner is... YOU. your cards are:{players['user']}, with a total of {sum(user_score_list)}")
			return winner	
	else:
		winner = (f" The winner is... YOU. your cards are:{players['user']}, with a total of {sum(user_score_list)}")
		return winner


def is_greater_than_21(n1):
	if sum(n1) > 21:
		is_greater_21 = True
		return is_greater_21
	else:
		is_greater_21 = False
		return is_greater_21	

def finish_game():
	print(winning_player(user_score_list, dealer_score_list))
	print(f" The dealer has: {dealer_score_list}, and a total of {sum(dealer_score_list)}.")

def keep_playing():
	end_of_game = False
	is_greater_21 = False
	while end_of_game == True:
		finish_game()	
	else:
		is_greater_than_21(user_score_list)
		if is_greater_21 == True:
			end_of_game = True
		else:
			user_get_another_card(cards)
			is_greater_than_21(user_score_list)
			if is_greater_21 == True:
				end_of_game = True
			else:
				is_greater_than_21(dealer_score_list)
				if is_greater_21 == True:
					end_of_game = True
				else:
					dealer_get_another_card(cards)	

			print(f" Your cards: {user_score_list}, current score: {sum(user_score_list)}, dealer's first card is {dealer_first_card}")
			should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
			if should_continue == "y":
				keep_playing()
			else:
				finish_game()
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == "y":
	user_get_another_card(cards)
	dealer_first_card = dealer_get_another_card(cards)
	# user_get_another_card(cards)
	#end_of_game = False
	keep_playing()
else:
	finish_game()		

	
		
	





