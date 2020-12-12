"""
This stores all the funtions which display something to the player.
"""


from time import sleep

def display_player(Trick_count, Trump_Card, player_hand,computer_Card="---", player_card="---"):
    print("-------------------------------------\n")
    print(f"Trick {Trick_count}")
    print(f"Trump suit : {Trump_Card}")
    display_card(computer_Card, "Computer")
    display_card(player_card, "Player")
    display_hand(player_hand)

def display_card(card, player):
    if card == "---":
        print(f"{player} played : {card}")
    else:
        # used of in the middle as it is more user friendly. "K of ♠" instead of "K♠"
        print(f"{player} played : {card[0]} of {card[1]}")

def display_hand(current_hand=[]):
    # This function displays all cards currently in player hand
    base_msg = "You have"
    if len(current_hand) == 0:
        base_msg += " 0 Cards left. "
    else:
        for card in (current_hand):
            base_msg += f" {card[0]} of {card[1]},"

    # slicing done to remove extra comma at the end when having cards listed
    base_msg = base_msg[:len(base_msg)-1]+"\n"

    print(base_msg)


def display_welcome_msg():
    print(    """
    888       888          888                                              888            
    888   o   888          888                                              888            
    888  d8b  888          888                                              888            
    888 d888b 888  .d88b.  888  .d8888b .d88b.  88888b.d88b.   .d88b.       888888 .d88b.  
    888d88888b888 d8P  Y8b 888 d88P"   d88""88b 888 "888 "88b d8P  Y8b      888   d88""88b 
    88888P Y88888 88888888 888 888     888  888 888  888  888 88888888      888   888  888 
    8888P   Y8888 Y8b.     888 Y88b.   Y88..88P 888  888  888 Y8b.          Y88b. Y88..88P 
    888P     Y888  "Y8888  888  "Y8888P "Y88P"  888  888  888  "Y8888        "Y888 "Y88P"  
                                                                                        
                                                                                       
                                                                                       
    """)
    sleep(1)
    print("""
                             .d88888b.  888b     d888 8888888
                            d88P" "Y88b 8888b   d8888   888
                            888     888 88888b.d88888   888
                            888     888 888Y88888P888   888
                            888     888 888 Y888P 888   888
                            888     888 888  Y8P  888   888
                            Y88b. .d88P 888   "   888   888
                             "Y88888P"  888       888 8888888
          """)
    sleep(0.5)

def display_player_won():
    print(
    """
      __   __                                _ 
      \ \ / /                               | |
       \ V /___  _   _  __      _____  _ __ | |
        \ // _ \| | | | \ \ /\ / / _ \| '_ \| |
        | | (_) | |_| |  \ V  V / (_) | | | |_|
        \_/\___/ \__,_|   \_/\_/ \___/|_| |_(_)
                                         
                                                                          
    """
    )

def display_computer_won():
    print(
    """
     _____                             _                                  _ 
    /  __ \                           | |                                | |
    | /  \/ ___  _ __ ___  _ __  _   _| |_ ___ _ __  __      _____  _ __ | |
    | |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| \ \ /\ / / _ \| '_ \| |
    | \__/\ (_) | | | | | | |_) | |_| | ||  __/ |     \ V  V / (_) | | | |_|
     \____/\___/|_| |_| |_| .__/ \__,_|\__\___|_|      \_/\_/ \___/|_| |_(_)
                        | |                                               
                        |_|                                               
    """
    )


def display_draw():
    print(
    """
     _____ _     _              ______                    _ 
    |_   _| |   (_)             |  _  \                  | |
      | | | |_   _ ___    __ _  | | | |_ __ __ ___      _| |
      | | | __| | / __|  / _` | | | | | '__/ _` \ \ /\ / / |
     _| |_| |_  | \__ \ | (_| | | |/ /| | | (_| |\ V  V /|_|
     \___/ \__| |_|___/  \__,_| |___/ |_|  \__,_| \_/\_/ (_)
                                                        
                                                        
    """
    )


def display_thank_you_message():
    print(
        """
        
  _____ _                 _                           __              ____  _             _              
 |_   _| |__   __ _ _ __ | | __  _   _  ___  _   _   / _| ___  _ __  |  _ \| | __ _ _   _(_)_ __   __ _  
   | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | | |_ / _ \| '__| | |_) | |/ _` | | | | | '_ \ / _` | 
   | | | | | | (_| | | | |   <  | |_| | (_) | |_| | |  _| (_) | |    |  __/| | (_| | |_| | | | | | (_| | 
   |_| |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| |_|  \___/|_|    |_|   |_|\__,_|\__, |_|_| |_|\__, | 
                                 |___/                                              |___/         |___/ 
                                      ___  __  __ ___   _                                                                   
                                     / _ \|  \/  |_ _| | |                                                                                  
                                    | | | | |\/| || |  | |                                                                                  
                                    | |_| | |  | || |  |_|                                                                                  
                                     \___/|_|  |_|___| (_)                                                                                  
                                                                                                                 
        
        """
    )
