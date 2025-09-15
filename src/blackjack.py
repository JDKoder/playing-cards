import random as r
import pydealer as pd
from player import Player
from rankdicts import BLACKJACK_RANKS
from card_rich import (convert_rich_cards_to_grid,
                            convert_face_to_rich_text, 
                            RICH_CARD_FACE)
from console import console as c
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


"""This is the blackjack game"""
def run_game():
    #initialize game variables
    round_count = 0
    deck = pd.Deck(rebuild=False, re_shuffle=True)
    player_hand = pd.Stack()
    dealer_hand = pd.Stack()
    discard_pile = pd.Stack()
    player = Player(player_hand, 10)
    dealer = Player(dealer_hand, 1000)

    #for i in range(26):
    while True:
        #Shuffle phase
        round_count += 1
        print(f"Round {round_count}")
        for i in range(20):
            deck.shuffle()
        #Wager phase
        # player chooses the wager and the dealer matches, all credits go into the pot
        # if the dealer can't match, the wager must be the maximum left in the dealers account and the 
        # remainder is returned to the player's credits
        player_wager = 10
        player_is_dipshit = True
        while player_is_dipshit:
            wager_input = input(f"Please place a bet in a denomination of 10 (you have {player.credits}): ")
            wager_value = 0
            try:
                wager_value = int(wager_input)
            except ValueError:
                continue
            if wager_value > player.credits:
                continue
            if wager_value > 0 and wager_value % 10 == 0:
                player_is_dipshit = False
                player_wager = wager_value

        dealer_wager = player_wager
        pot = 0
        if dealer.credits < player_wager:
            print(f"dealer will match up to {dealer.credits}")
            player_wager = dealer.credits
            dealer_wager = dealer.credits

        # Finalize Bet phase
        print(f"player wagers {player_wager}")
        pot += player.take_credits(player_wager)
        print(f"dealer meets {dealer_wager}")
        pot += dealer.take_credits(dealer_wager)


        #Deal phase
        #Alternate drawing cards for the player and the dealer
        player_hand += deck.deal(1)
        print(f"Player is dealt {player_hand[0]}")
        dealer_hand += deck.deal(1)
        print(f"Dealer is dealt {dealer_hand[0]}")
        player_hand += deck.deal(1)
        print(f"Player is dealt {player_hand[1]}")
        dealer_hand += deck.deal(1)
        print(f"Dealer is dealt a face down card")

        player_hand_display = []
        player_hand_display.append(convert_face_to_rich_text(RICH_CARD_FACE[player_hand.cards[0].value],player_hand.cards[0].suit))
        player_hand_display.append(convert_face_to_rich_text(RICH_CARD_FACE[player_hand.cards[1].value],player_hand.cards[1].suit))
        #c.print(convert_rich_cards_to_grid(player_hand_display))
        players_hand_grid = convert_rich_cards_to_grid(player_hand_display)
        #c.print(players_card)

        COLOR_PALETTE = {
            "lightgoldenrodyellow": "rgb(250,250,210)",
            "darkgreen": "rgb(0,100,0)"
        }
        player_panel = Panel(players_hand_grid, title="Player", title_align="left", style=f"{COLOR_PALETTE['lightgoldenrodyellow']} on {COLOR_PALETTE['darkgreen']}")

        dealer_hand_display = []
        dealer_hand_display.append(convert_face_to_rich_text(RICH_CARD_FACE[dealer_hand.cards[0].value],dealer_hand.cards[0].suit))
        dealer_hand_display.append(convert_face_to_rich_text(RICH_CARD_FACE["Back"], "Back"))
        dealers_hand_grid = convert_rich_cards_to_grid(dealer_hand_display)
 
        dealer_panel = Panel(dealers_hand_grid, title="Dealer", title_align="left", style=f"{COLOR_PALETTE['lightgoldenrodyellow']} on {COLOR_PALETTE['darkgreen']}")

        """ Input: List of Card
            Return: Integer value of all cards combined
            
            Totals the value of the cards in the hand.
            reduce aces to lowest value (1) if the hand would lose otherwise
            """
        def get_hand_value(cards):
            total = 0
            ace_count = 0
            for card in cards:
                if card.value == "Ace":
                    ace_count += 1
                total += BLACKJACK_RANKS[card.value]
            #reduce aces to lowest value if the hand would lose otherwise
            while total > 21 and ace_count > 0:
                total -= 10
                ace_count -= 1
            return total


        player_hand_value = get_hand_value(player_hand)
        dealer_hand_value = get_hand_value([dealer_hand.cards[0]])
        
        stats = f"Player Hand: {player_hand_value}\nDealer Hand: {dealer_hand_value}"
        stats_panel = Panel(Text(stats), title=f"Game {round}")

        table_grid = Table.grid(expand=True)
        table_grid.add_column()
        table_grid.add_column()
        table_grid.add_column()
        table_grid.add_row(player_panel, dealer_panel, stats_panel)
        c.print(table_grid)

        #Hit or Stay
        #TODO IMPLEMENT HIT STAY LOOP
        

        #Dealer Flips and hits to at least 16


        #Can Play Again?
        print(f"Player's remaining credits: {player.credits}")
        if player.credits < 10 or dealer.credits < 10:
            print(f"Not enough credits to play again.")
            if player.credits >= 10:
                print("Player Takes the House!")
            else:
                print("You're broke!  Game Over")
            break
        
