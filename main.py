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
user_score_list = []
dealer_score_list = []


def get_card(player):
    """Return a random card value"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    player.append(card)
    return card


def check_for_11(player):
    '''check for the appearance of card"11" and, if total score > 21, replaces value to one.'''
    if 11 in player:
        if sum(player) > 21:
            for item in player:
                if item == 11:
                    card_index = player.index(item)
                    player[card_index] = 1
                    return player


def check_winner(n1, n2):
    '''compare scores and and checks game logic to define winner'''
    user_score = sum(n1)
    dealer_score = sum(n2)
    if user_score > 21 and dealer_score < 21:
        winner = ("dealer")
        return winner
    elif user_score > 21 and dealer_score > 21:
        winner = ("tie")
        return winner
    elif user_score < 21 and dealer_score < 21:
        if user_score > dealer_score:
            winner = ("user")
            return winner
        elif user_score < dealer_score:
            winner = ("dealer")
            return winner
        elif user_score == dealer_score:
            winner = ("tie")
            return winner
    elif user_score < 21 and dealer_score > 21:
        winner = ("user")
        return winner
    elif user_score == 21 and dealer_score < 21:
        winner = ("user")
        return winner
    elif user_score == 21 and dealer_score == 21:
        winner = ("tie")
        return winner
    elif user_score == 21 and dealer_score > 21:
        winner = ("user")
        return winner
    elif user_score > 21 and dealer_score == 21:
        winner = ("dealer")
        return winner
    elif user_score < 21 and dealer_score == 21:
        winner = ("dealer")
        return winner


def keep_playing():
    while sum(user_score_list) < 21 and sum(dealer_score_list) < 21:
        print(
            f'Your total score is {sum(user_score_list)}, your cards are:{user_score_list}')
        print(f"Dealer's first card is {dealer_first_card}")
        should_continue = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        if should_continue == 'y':
            get_card(user_score_list)
            if sum(dealer_score_list) <= 17:
                get_card(dealer_score_list)
        else:
            if sum(dealer_score_list) <= 17:
                get_card(dealer_score_list)
                check_for_11(user_score_list)
                check_for_11(dealer_score_list)
                if sum(user_score_list) < 21 and sum(dealer_score_list) < 21:
                    keep_playing()
                    # print( f'The winner is {check_winner(user_score_list, dealer_score_list)}')
            else:
                if should_continue == 'n':
                    check_for_11(user_score_list)
                    check_for_11(dealer_score_list)
                    print(
                        f'The winner is {check_winner(user_score_list, dealer_score_list)}')
                    break
    else:
        check_for_11(user_score_list)
        check_for_11(dealer_score_list)
        if sum(user_score_list) < 21 and sum(dealer_score_list) < 21:
            keep_playing()
        else:
            return print(f'The winner is {check_winner(user_score_list, dealer_score_list)}')


start_game = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':
    get_card(user_score_list)
    dealer_first_card = get_card(dealer_score_list)
    get_card(user_score_list)
    keep_playing()

print(
    f'User score list = {user_score_list} /n Dealer score list = {dealer_score_list}')	
		

	
		
	



