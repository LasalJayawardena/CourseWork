"""
This is where most of the validastion function are written:
eg. For to check user follows rules and to sanitize user input
"""

import re
from display_func import display_player, display_hand


def validate_trick_play(computer_Card, player_card, player_deck):
    # check if player puts same suit as computer
    # check if player has card from the suit which the computer selected, if so then return false
    # if the player does not ave then he can play any card
    if computer_Card[1] != player_card[1]:
        suit = computer_Card[1]
        card_With_suit = [c for c in player_deck if c[1] == suit]
        if len(card_With_suit) > 0:
            return False
    return True

def sanitize_user_input(card, upper_bound=2, **kwargs):
    # The reason to include kwargs was that of a special case when the card number is 10
    # When the card is 10, I check for a certain parameter in kwargs and add an extra character instead of the usual upper bpund

    # Functionality to remove all spaces : leading, trailing and all irregular spaces in between
    # used regex as it was cleaner and easier to implement
    card = re.sub(r'\s*', '', card)
    card = card.capitalize()
    sanitized_card = card
    if len(card) > upper_bound:
        # Small improvement to get the specifed length, the upperbound,  characters of card after removing spaces
        sanitized_card = card[:upper_bound]
        if(kwargs and kwargs["c_in_deck"] == True):
            if(card[1] == '0'):
                # eg: If user inputs "    10   ♠opfp c"
                # it will sanitize to "10♠"
                sanitized_card = card[:upper_bound+1]

    return sanitized_card


def check_card_in_hand(current_hand, card):

    # Check if the card is in list: check if atleast one true, meaning card in deck then return true else false
    in_deck = any((card == x[0]+x[1] for x in current_hand))
    return(in_deck)


def validate_trump_suit():
    suits = ("♠", "♣", "♥", "♦")
    # check if the trump selected is a valid suit
    while True:
        trump_selection = input("Please enter the trump suit:\n")
        trump_selection = sanitize_user_input(trump_selection, 1)
        if trump_selection in suits:
            break
        print("\nPlease choose a valid suit as Trumps\n")
    return trump_selection


def validate_for_Card_in_Deck(Trick_count, Trump_Card, player_hand, computer_card="---"):

    # check if the card selected by player is in their deck
    while True:
        card_chosen = input("Please enter the Card for this trick:\n")
        card_chosen = sanitize_user_input(card_chosen, 2, c_in_deck=True)
        if check_card_in_hand(player_hand, card_chosen) == True:
            if len(card_chosen) == 2:
                return (card_chosen[0], card_chosen[1])
            else:
                # special case when a number card of 10 is selected
                return (card_chosen[0:len(card_chosen)-1], card_chosen[-1])
            break
        print("\nPlease choose a valid card in your deck!\n")
        # show user the trump and the available cards
        display_player(Trick_count, Trump_Card, player_hand, computer_card)
        


