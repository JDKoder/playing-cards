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
from rich.prompt import Prompt, Confirm


"""This is the blackjack game"""
def run_game():
    c.clear()
    #initialize game variables
    round_count = 0
    deck = pd.Deck(rebuild=False, re_shuffle=True)
    player_hand = pd.Stack()
    dealer_hand = pd.Stack()
    discard_pile = pd.Stack()
    player = Player(player_hand, 10)
    dealer = Player(dealer_hand, 1000)

    def reset_game():
        """In a game over state, this function provides a way to reset the game state to keep playing."""
        c.clear()
        nonlocal round_count
        nonlocal deck
        nonlocal player_hand
        nonlocal discard_pile
        nonlocal player
        nonlocal dealer
        nonlocal dealer_hand
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
        pot += player.take_credits(player_wager)
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


        def hand_to_display_grid(title, cards, hide=False):
            player_hand_display = []
            for i in range(len(cards)):
                if i > 0 and hide:
                    player_hand_display.append(convert_face_to_rich_text(RICH_CARD_FACE["Back"], "Back"))
                else:
                    player_hand_display.append(convert_face_to_rich_text(RICH_CARD_FACE[cards[i].value],cards[i].suit))
            return convert_rich_cards_to_grid(player_hand_display)

        COLOR_PALETTE = {
            "lightgoldenrodyellow": "rgb(250,250,210)",
            "darkgreen": "rgb(0,100,0)"
        }
        player_panel = None
        dealer_panel = None
        def update_panels(dealer_hides=False):
            nonlocal player_panel
            nonlocal dealer_panel
            players_hand_grid = hand_to_display_grid("Player", player_hand.cards)
            dealers_hand_grid = hand_to_display_grid("Dealer", dealer_hand.cards, dealer_hides)
            player_panel = Panel(players_hand_grid, title="Player", title_align="left", style=f"{COLOR_PALETTE['lightgoldenrodyellow']} on {COLOR_PALETTE['darkgreen']}")
            dealer_panel = Panel(dealers_hand_grid, title="Dealer", title_align="left", style=f"{COLOR_PALETTE['lightgoldenrodyellow']} on {COLOR_PALETTE['darkgreen']}")

        update_panels(True)

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

        def update_ui(player_hand, dealer_hand):
            nonlocal round_count
            nonlocal player_panel
            nonlocal dealer_panel
            nonlocal pot
            player_hand_value = get_hand_value(player_hand)
            dealer_hand_value = get_hand_value(dealer_hand)

            stats = f"Player Hand: {player_hand_value}\nDealer Hand: {dealer_hand_value}\nCurrent Bet: {player_wager}\nPot: {pot}"
            stats_panel = Panel(Text(stats), title=f"Game {round_count}")

            table_grid = Table.grid(expand=True)
            table_grid.add_column()
            table_grid.add_column()
            table_grid.add_column()
            table_grid.add_row(player_panel, dealer_panel, stats_panel)
            c.clear()
            c.print(table_grid)

        """Player Hit or Stay"""
        while True:
            update_ui(player_hand, [dealer_hand.cards[0]])

            hit_choices = ["hit", "h"]
            stay_choices = ["stay", "s"]
            hit_stay_choices = hit_choices.append(stay_choices)
            command = Prompt.ask(Text("Hit (").append(" h ", style="red on blue").append(") or Stay (").append(" s ", style="red on blue").append(")"), choices=hit_stay_choices, case_sensitive=False)
            
            if command.lower() in hit_choices:
                player_hand += deck.deal(1)
                c.print(f"Player draws the {player_hand[len(player_hand)-1]}")
                if get_hand_value(player_hand) > 21:
                # Player loses
                    update_panels(False)
                    update_ui(player_hand, dealer_hand)
                    c.print("Hand is more than 21!")
                    break
                update_panels(True)
            elif command.lower() in stay_choices:
                update_panels(False)
                c.print("Player stays")
                c.print("Dealer shows their hand")
                update_ui(player_hand, dealer_hand)
                break


        """
        Dealer AI
        Dealer draws to at least 16 while they are losing to the player.  
        If the hands are even, the dealer will push unless their own hand value is less than 11,
        guaranteeing them the win if they hit.
        """
        def ai_hit(dealer_hand_value, player_hand_value):
            absolute_hit = dealer_hand_value < 11
            conditional_hit = dealer_hand_value < 16 and player_hand_value > dealer_hand_value and player_hand_value <= 21
            return absolute_hit or conditional_hit

        while ai_hit(get_hand_value(dealer_hand), get_hand_value(player_hand)):
            c.print("Dealer hits")
            dealer_hand += deck.deal(1)
            c.print(f"Dealer draws the {dealer_hand[len(dealer_hand)-1]}")
            update_panels(False)
            update_ui(player_hand, dealer_hand)

        dealer_hand_value = get_hand_value(dealer_hand)
        player_hand_value = get_hand_value(player_hand)

        #Check win conditions
        player_over = player_hand_value > 21
        if player_over:
            c.print("[bold red]Player Loses!  Your hand was over 21[/bold red]")
        elif player_hand_value == dealer_hand_value:
            # push
            c.print("[bold]Push! Wager is returned.[/bold]")
            player.credits += player_wager
            dealer.credits += dealer_wager
        elif player_hand_value > dealer_hand_value or dealer_hand_value > 21:
            # Player Wins
            c.print("[bold green]Player wins the round[/bold green]")
            player.credits += pot
        elif player_hand_value < dealer_hand_value:
            # Player Loses
            c.print("[bold]Player Loses!  Your hand was beaten.[/bold]")
            dealer.credits += pot


        def escape_message():
            c.clear()
            c.print("Thank you for playing Blackjack with me!")

        #Can Play Again?
        print(f"Player's remaining credits: {player.credits}")
        if player.credits < 10 or dealer.credits < 10:
            print(f"Not enough credits to play again.")
            if player.credits >= 10:
                c.print("[bold yellow on black]Player Takes the House![/bold yellow on black]")
            else:
                c.print("[bold white on red]You're broke!  Game Over[/bold white on red]")
            restart_game = Confirm.ask("Do you want to play again?")
            if restart_game:
                reset_game()
                c.clear()
                continue
            else:
                escape_message()
                break
        else:
            print(f"Player discards {len(player_hand)} cards from hand")
            discard_pile += player_hand.deal(len(player_hand))
            print(f"Dealer discards {len(dealer_hand)} hand")
            discard_pile += dealer_hand.deal(len(dealer_hand))
            print("Shuffling and Returning the discard pile to main deck.")
            discard_pile.shuffle()
            deck += discard_pile.deal(len(discard_pile))
            print(f"{deck.size} cards ready for the next game.")
        play_again = Confirm.ask("Another hand?",console=c) 
        if not play_again:
            escape_message()
            break
        else: 
            c.clear()
    return True
