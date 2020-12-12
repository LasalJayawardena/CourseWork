"""
This is a two player OMI Game between computer and player
"""



from deck import intialize_deck, deal_cards
from game_logic import computer_lead, player_lead
from display_func import display_welcome_msg, display_hand, display_player_won, display_computer_won, display_player, display_draw, display_thank_you_message
from validate_func import validate_trump_suit
from computer import choose_trump
import sys
# Player has freedom to choose trumps

def main():
    
    # Displays Welcome message
    display_welcome_msg()
    # This is to identify who will tell the trumps
    trump_announce = "player"
    # This is to identify who will lead the trick, this changes every trick
    game_trick_player = "computer"
    while True:
        # intialize scores and the game deck
        Computer_Score = 0
        Human_Score = 0
        game_deck = intialize_deck()

        # This when all 8 tricks begin, and the most of the game logic is implemented
        game_tricks(game_deck, Computer_Score, Human_Score,game_trick_player, trump_announce)

        # Switch trump annouonce and game_trick players after 8 tricks, when player wants to play agian
        if trump_announce == "player":
            trump_announce = "computer"
            game_trick_player = "player"
        else:
            trump_announce = "player"
            game_trick_player = "computer"

        # Clear deck after each round( after 8 tricks )
        game_deck.clear()

        # Ask user if he wants play agian 
        user_input = input("Do you want to play anothe round? (y/n)").strip().lower()[0]
        print("\n")
        if user_input == 'n':
            break



def game_tricks(game_deck, Computer_Score, Human_Score, game_trick_player, trump_announce):
    NUMBER_OF_TRICKS = 8
    # This when all the 8 tricks will happen
    for i in range(1, NUMBER_OF_TRICKS+1):
        Trick_count = i
        if game_trick_player == "computer":
            if Trick_count == 1 and trump_announce == "player":
                # deal 4 decks for player
                player_hand = deal_cards(game_deck, 4)
                display_hand(player_hand)
                Trump_Card = validate_trump_suit()

                # deal the next 4 cards
                player_hand += deal_cards(game_deck, 4)
                # deal 8 cards for the computer
                computer_hand = deal_cards(game_deck, 8)
            winner = computer_lead(game_deck, Trick_count, player_hand, computer_hand, Trump_Card)

        else:
            if Trick_count == 1 and trump_announce == "computer":
                computer_hand = deal_cards(game_deck, 4)
                Trump_Card = choose_trump(computer_hand)
                print(f"Computer chose trump as {Trump_Card}\n")

                computer_hand += deal_cards(game_deck, 4)
                player_hand = deal_cards(game_deck, 8)
                
            display_player(Trick_count, Trump_Card, player_hand)
            print("You lead the trick!")

            winner = player_lead(game_deck, Trick_count, player_hand, computer_hand, Trump_Card)

        if winner == "You won":
            game_trick_player = "player"
            Human_Score += 2
            print("Player +2")
        else:
            game_trick_player = "computer"
            Computer_Score += 2
            print("Computer +2")

        print("Computer score is {}".format(Computer_Score))
        print("Your score is {}\n\n".format(Human_Score))

    # Check the winner after all tricks
    game_result(Computer_Score, Human_Score)



def game_result(Computer_Score, Human_Score):
    # display appropriate output after 8 tricks
    print("Computer score is {} / Player score is {}".format(Computer_Score, Human_Score))
    if Computer_Score > Human_Score:        
        display_computer_won()
    elif Computer_Score < Human_Score:
        display_player_won()
    else:
        display_draw()    
    
if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        display_thank_you_message()
        sys.exit(0)
    else:
        display_thank_you_message()