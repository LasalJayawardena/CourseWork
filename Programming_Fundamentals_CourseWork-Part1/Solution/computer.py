"""
This is where most of the function needed by the computer is written
"""

from random import choice

def play_card(card_deck):
    # This is when the computer's turn to lead the trick
    return choice(card_deck)


def computer_play_card(c_deck, player_card, trump):
    suit_ace_dict = {'J': "11", 'Q': "12", 'K': "13", 'A': "14"}
    # check whether similar cards
    similar = [c for c in c_deck if c[1] == player_card[1]]
    # all cards with trump
    trump = [c for c in c_deck if c[1] == trump]
    # all other card other than trumps, usefule when no similar cards
    other = [c for c in c_deck if (c[1] != player_card[1]) and (c[1] != trump)]

    # check if there are similar cards
    if len(similar) > 0:

        higher = []
        # logic to get all similar cards higher than the player card
        # nested if conditions needed to give value to ace and picture cards and then compare
        for card in similar:
            if (suit_ace_dict.get(card[0])):
                if suit_ace_dict.get(player_card[0]):
                    if int(suit_ace_dict[card[0]]) > int(suit_ace_dict[player_card[0]]):
                        higher.append(card)
                else:
                    if int(suit_ace_dict[card[0]]) > int(player_card[0]):
                        higher.append(card)
            else:
                if suit_ace_dict.get(player_card[0]):
                    if int(card[0]) > int(suit_ace_dict[player_card[0]]):
                        higher.append(card)
                else:
                    if int(card[0]) > int(player_card[0]):
                        higher.append(card)

        if len(higher) > 0:
            # if there are cards higher than the card the player played
            # return lowest of them all, which will still win
            highest_lower = get_lowest_card(higher)
            return highest_lower
        else:
            # if there no cards higher than the card the player playes
            # then give the lowest card of that suit
            lowest_card = get_lowest_card(similar)
            return lowest_card

    # check for trump options
    # this is when the computer does not have cards for the suit the player played
    elif len(trump) > 0 and player_card[1] != trump:
        # return the lowest trump card availbale in computers hand
        lowest_trump = get_lowest_card(trump)
        return lowest_trump

    # lowest in other cards
    else:
        # this when the computer does not have card swith the player suit or trumps
        # so get the cards with lowest value in all suits
        lowest_other = get_lowest_card(other)
        lowest_available = [c for c in other if c[0] == lowest_other[0]]
        # randomly return card from the set of lowest ard values if there multiple cards
        return choice(lowest_available)


def get_lowest_card(deck):
    # returns lowest card from a given deck
    suit_ace_dict = {'J': "11", 'Q': "12", 'K': "13", 'A': "14"}
    lowest = deck[0]
    # nested ifs needed because the picture cards and aces dont have a value
    for card in deck:
        if (suit_ace_dict.get(card[0])):
            if(suit_ace_dict.get(lowest[0])):
                if int(suit_ace_dict[card[0]]) < int(suit_ace_dict[lowest[0]]):
                    lowest = card
            else:
                if int(suit_ace_dict[card[0]]) < int(lowest[0]):
                    lowest = card
        else:
            if(suit_ace_dict.get(lowest[0])):
                if int(card[0]) < int(suit_ace_dict[lowest[0]]):
                    lowest = card
            else:
                if int(card[0]) < int(lowest[0]):
                    lowest = card
    return lowest



def choose_trump(hand):
    suit_occurence = {"♠": 0, "♣": 0, "♥": 0, "♦": 0}
    # This will create a dict with number of cards for each suit
    for c in hand:
        if(suit_occurence.get(c[1]) != None):
            suit_occurence[c[1]] += 1

    # Find the maximum value of the occurence in each suit
    suit_most_occur = max(suit_occurence, key=suit_occurence.get)
    # get the number of card for the suit which had the highest occurence
    # helpful dealing when more than one suit has the most occurence
    max_val = suit_occurence[suit_most_occur]

    # Calculate how mny suits with the max occurence
    num_max = 0
    for i in suit_occurence.items():
        if i[1] == max_val:
            num_max += 1

    # check if a single suit occurs three times then return
    if max_val >= 3:
        return suit_most_occur

    # check if two suits have the max occurence meaning two cards for both suits
    elif max_val == 2 and num_max == 2:
        # get both suit with the most occurence into an array
        suits = [i[0] for i in suit_occurence.items() if i[1] == max_val]
        # check if the cards of first suit have an Ace
        ace_in_suit_1 = any(i[0] == 'A' for i in hand if i[1] == suits[0])
        # check if the cards of second suit have an Ace
        ace_in_suit_2 = any(i[0] == 'A' for i in hand if i[1] == suits[1])
        if ace_in_suit_1:
            # return second suit if first has ace... Followed the cw tactics
            return suits[1]
        if ace_in_suit_2:
            # return first suit if second suit has ace... Followed the cw tactics
            return suits[0]

        # This will calculate the total value for the cards in each suit
        # Add all card values and even the picture cards and ace is given a value

        suit1_score = calculate_suit_sum(hand, suits[0])
        suit2_score = calculate_suit_sum(hand, suits[1])
        if suit1_score > suit2_score:
            # If the the first suit has cards with higher value then return it
            return suits[0]
        elif suit1_score < suit2_score:
            # If the the second suit has cards with higher value then return it
            return suits[1]
        else:
            # If both suit have cards with equal value then use
            # get the cards for each suit separately
            suit1 = [i for i in hand if i[1] == suits[0]]
            suit2 = [i for i in hand if i[1] == suits[1]]
            # Then I calculated the range of the cards
            # This is an improvement: Reason is
            # eg: It is better to have Q and 7 instead of J and 8
            # Eben thought they have the same value the first set is better
            suit1_range = calculate_suit_range(suit1)
            suit2_range = calculate_suit_range(suit2)

            if suit1_range > suit2_range:
                # So if the values of the cards are far apart for suit1 then return the suit as trumps
                return suits[0]
            elif suit1_range < suit2_range:
                # So if the values of the cards are far apart for suit2 then return the suit as trumps
                return suits[1]

            # Last case the the cards are same for both suits:
            # So used a random choice from random module to select one suit between the two
            return choice(suits)

    elif max_val == 2 and num_max == 1:
        # This when one suit has two cards but the other suits to has one card each
        # Accordind to cw tactics they have told that if the two cards are lower then,
        # The players choose the suit with no cards, hoping to get those cards in the second deal
        # My assumption was if both the two cards were between 7 and 10 incluive then to choose hte other suit

        #  chose the suit with most cards
        max_suit = [i[0] for i in suit_occurence.items() if i[1] == max_val][0]

        #  select all cards which have the max_suit
        max_suit_deck = [i for i in hand if i[1] == max_suit]

        # got the numeric total of the cards, including picture cards and ace
        suit_total = calculate_suit_sum(hand, max_suit)
        # got the averge of the cards
        avg_suit = round(suit_total / 2)
        # got the range of the two cards
        range_suit = calculate_suit_range(max_suit_deck)
        if avg_suit < 10 and range_suit <= 3:
            min_suit_deck = [i[0] for i in suit_occurence.items() if i[1] == 0]
            return min_suit_deck[0]
        return max_suit
    else:
        lowest = get_lowest_card(hand)[0]
        lowest_card = [c for c in hand if c[0] == lowest]
        return choice(lowest_card)[1]


def calculate_suit_sum(cards, suit):
    # Helps to implement in finding the sum of all cards
    suit_ace_dict = {'J': "11", 'Q': "12", 'K': "13", 'A': "14"}
    total = 0
    for c in cards:
        if c[1] == suit:
            if (suit_ace_dict.get(c[0])):
                total += int(suit_ace_dict[c[0]])
            else:
                total += int(c[0])
    return total


def calculate_suit_range(deck):
    # calculate the range of given cards include the picture cards and the Aces
    # needed when choosing trumps

    # nested if conditions needed to map a value to picture cards and aces 
    suit_ace_dict = {'J': "11", 'Q': "12", 'K': "13", 'A': "14"}
    card1 = deck[0]
    card2 = deck[1]
    if suit_ace_dict.get(card1[0]):
        if suit_ace_dict.get(deck[1][0]):
            return abs(int(suit_ace_dict[card1[0]]) - int(suit_ace_dict[card2[0]]))
        else:
            return abs(int(suit_ace_dict[card1[0]]) - int(card2[0]))
    else:
        if suit_ace_dict.get(card2[0]):
            return abs(int(card1[0]) - int(suit_ace_dict[card2[0]]))
        else:
            return abs(int(deck[0][0]) - int(deck[1][0]))
