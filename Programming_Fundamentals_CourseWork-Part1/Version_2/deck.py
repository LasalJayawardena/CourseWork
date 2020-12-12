"""
This is where the common function invlving the deck are stored.

"""

import itertools
import random


def shuffle_deck(deck):
    # Implemented Fisher–Yates algorithm to shuffle the cards
    # Because it has a Time complexity of O(n) and the after the shuffle the randomness is also good

    # counter set at at length of deck -1
    start_counter = len(deck) - 1
    for index in range(start_counter, 0, -1):
        # generate random index
        rand_index = random.randint(0, index)
        # switch card on index with card on the randomly generated index
        deck[index], deck[rand_index] = deck[rand_index], deck[index]


def intialize_deck():
    suits = ("♠", "♣", "♥", "♦")
    numbers = ("A", "K", "Q", "J", "10", "9", "8", "7")
    # This is for reference only : symbol_dict= {"clubs":'♣', "diamonds":"♦", "hearts":"♥","spades":"♠"}

    # Chose itertools for readability
    deck = list(itertools.product(numbers, suits))
    # deck = [(x,y) for x in suits for y in numbers]

    # Perform a inplace shuffle using the shuffle_deck function defined above
    shuffle_deck(deck)

    return deck


def deal_cards(deck, number_to_Deal=0):
    # copy deck
    clone_deck = deck.copy()

    # Simulate the card being removed from top
    for i in range(number_to_Deal):
        deck.pop(0)

    # Could have created a list and added the poped values but chose this as method looks cleaner
    return clone_deck[:number_to_Deal]


def check_trick_winner(player_card, computer_card, trump, trick_leader="player"):
    suit_ace_dict = {'J': "11", 'Q': "12", 'K': "13", 'A': "14"}

    # case when the two suits of the cards are same
    if player_card[1] == computer_card[1]:

        # Nested if conditions needed as the cards need to be mapped by the dictionary
        # Reason is to give the picture card and aces a value

        # Enter when the first card of the pair is a picture card or ace
        if (suit_ace_dict.get(player_card[0])):
            # Enter when the first card and the second cards of the pair are a picture card or ace
            if(suit_ace_dict.get(computer_card[0])):
                if int(suit_ace_dict[player_card[0]]) > int(suit_ace_dict[computer_card[0]]):
                    return "You won"
                return "Computer won"
            # Enter when the first card of the pair is a picture card or ace and the second is a number card
            else:
                if int(suit_ace_dict[player_card[0]]) > int(computer_card[0]):
                    return "You won"
                return "Computer won"

        # Enter when the first card of the pair is a number card 
        else:
            # Enter when the first card of the pair is a number card and the second is a colored card or ace
            if(suit_ace_dict.get(computer_card[0])):
                if int(player_card[0]) > int(suit_ace_dict[computer_card[0]]):
                    return "You won"
                return "Computer won"
            else:
                # Enter when the both cards of the pair are number cards 
                if int(player_card[0]) > int(computer_card[0]):
                    return "You won"
                return "Computer won"
    # this is when the player enter a trump and computer has another suit
    elif player_card[1] == trump and computer_card[1] != trump:
        return "You won"
    # this is when the computer enters a trump and player has another suit
    elif player_card[1] != trump and computer_card[1] == trump:
        return "Computer won"
    else:
    # When both player and computer have different cards and both are not trumps
        if trick_leader == "player":
            return "You won"
        return "Computer won"

"""
try:
    case1 = check_trick_winner(("K", "♥"), ("9", "♥"), "♠", "computer")
    assert case1 == "You won", "Case 1 failed"

    case2 = check_trick_winner(("8", "♦"), ("9", "♦"), "♦", "player")
    assert case2 == "Computer won", "Case 2 failed"
        
    case3 = check_trick_winner(("10", "♣"), ("J", "♥"), "♣", "computer")
    assert case3 == "You won", "Case 3 failed"

    case4 = check_trick_winner(("Q", "♦"), ("9", "♥"), "♥", "computer")
    assert case4 == "Computer won", "Case 4 failed"

    case5 = check_trick_winner(("Q", "♠"), ("A", "♦"), "♥", "player")
    assert case5 == "You won", "Case 5 failed"

    case6 = check_trick_winner(("10", "♦"), ("10", "♠"), "♣", "computer")
    assert case6 == "Computer won", "Case 6 failed"

except AssertionError as e:
    print(e)

else:
    print("All test cases pass")
    # All test cases pass
"""