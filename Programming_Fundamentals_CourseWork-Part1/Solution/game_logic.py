"""
This is where the game logic is avilable dor each scenario:
1) When the computer leads
2) When the player leads

"""

from deck import check_trick_winner
from validate_func import validate_for_Card_in_Deck, validate_trump_suit, validate_trick_play
from display_func import display_hand, display_welcome_msg, display_player
from computer import computer_play_card, get_lowest_card, choose_trump, play_card


# This is when player leads a trick
def player_lead(game_deck, trick_count, player_hand, computer_hand, Trump_Card):

    # This is when the player enters the card and it is checked whether card is in player's hand
    player_card = validate_for_Card_in_Deck(trick_count, Trump_Card, player_hand)
    # remove the selected card from players hand
    player_hand.remove(player_card)
    # this when the computer plays its card relaative to players card
    computer_card = computer_play_card(computer_hand, player_card, Trump_Card)
    # remove the selected card from computers' hand
    computer_hand.remove(computer_card)
    print("\n\n")
    # Display message with trick number, the cards played and the current player hand
    display_player(trick_count, Trump_Card, player_hand, computer_card, player_card)
    # print who won the trick
    winner = check_trick_winner(player_card, computer_card, Trump_Card)
    print(winner)
    # return who won the trick
    return winner




def computer_lead(game_deck, Trick_count, player_hand, computer_hand, Trump_Card):

    # computer leads the trick
    computer_card = play_card(computer_hand)
    # remove the selected card
    computer_hand.remove(computer_card)
    # Display message with trick number, the cards played and the current player hand
    display_player(Trick_count, Trump_Card, player_hand, computer_card)


    # Enter the player choice and check if card is in deck
    player_card = validate_for_Card_in_Deck(Trick_count, Trump_Card, player_hand, computer_card)
    # check whether the player followed the OMI rules
    valid = validate_trick_play(computer_card, player_card, player_hand)
    # below repeats above process until all conditions are met
    while not valid:
        display_player(Trick_count, Trump_Card, player_hand, computer_card)
        print(f"Follow the rules, cannot put a card of different suit if you have same suit.\nPlay card with suit {computer_card[1]}")
        player_card = validate_for_Card_in_Deck(Trick_count, Trump_Card, player_hand, computer_card)
        valid = validate_trick_play(computer_card, player_card, player_hand)
    # remove the card the player played
    player_hand.remove(player_card)


    # Display message with trick number, the cards played and the current player hand
    display_player(Trick_count, Trump_Card, player_hand, computer_card, player_card)
    # print who won the trick
    winner = check_trick_winner(player_card, computer_card, Trump_Card, "computer")
    print(winner)
    # return who won the trick
    return winner
