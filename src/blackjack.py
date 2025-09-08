import random as r
import pydealer as pd
from pydealer.const import POKER_RANKS
from player import Player
from rankdicts import BLACKJACK_RANKS
from card_ascii import print_cards
from card_rich import (convert_rich_cards_to_grid,
                            convert_face_to_rich_text, 
                            RICH_CARD_FACE)
from console import console as c
from rich import print


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
        c.print(convert_rich_cards_to_grid(player_hand_display))
        #c.print(players_card)


        dealer_hand_display = []
        dealer_hand_display.append(convert_face_to_rich_text(RICH_CARD_FACE[dealer_hand.cards[0].value],dealer_hand.cards[0].suit))
        dealer_hand_display.append(convert_face_to_rich_text(RICH_CARD_FACE["Back"], "Back"))
        c.print(convert_rich_cards_to_grid(dealer_hand_display))
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

        #player chooses a to bet "high" or "low"
        player_bet = "high"
        player_is_dur_dur_dur = True
        while player_is_dur_dur_dur:
            high_low_input = input("Choose \'h\' for \'High\' or \'l\' for \'Low\'(h/l): ")
            if not(high_low_input.lower() == 'h' or high_low_input.lower() == 'l'):
                continue
            match high_low_input.lower():
                case 'h':
                    player_bet = "high"
                case 'l':
                    player_bet = "low"
                case _:
                    continue
            player_is_dur_dur_dur = False

        print(f"Player's bet is {player_bet}")
        print(f"The Ace Standard Coin value is revealed: {ace_standard_coin}")
        print(f"Dealer shows their hand")
        print(f"Dealer's card is {dealer_hand[0]}")
        c.print(convert_rich_cards_to_grid([players_card, dealers_card]))

        #Finalize value of cards
        if player_hand[0].value == "Ace":
           player_hand[0].value = "Ace " + ace_standard_coin
        if dealer_hand[0].value == "Ace":
           dealer_hand[0].value = "Ace " + ace_standard_coin

        #whose card is higher
        
        if player_bet == "high" and player_hand[0].gt(dealer_hand[0], HIGH_LOW_RANKS):
            #player won
            print(f"Player wins! {player_hand[0].value} is higher than {dealer_hand[0].value}")
            print(f"Payout {pot}")
            player.award_credits(pot) 
        elif player_bet == "low" and player_hand[0].lt(dealer_hand[0], HIGH_LOW_RANKS):
            #player won
            print(f"Player wins! {player_hand[0].value} is lower than {dealer_hand[0].value}")
            print(f"Payout {pot}")
            player.award_credits(pot)
        elif player_hand[0].eq(dealer_hand[0], HIGH_LOW_RANKS):
            print(f"Hands are equal.  Push.")
            print(f"Payout {player_wager}")
            player.award_credits(player_wager)
            dealer.award_credits(dealer_wager)
        else:
            str_val = "lower"
            if (player_bet == "low"):
                str_val = "higher"
            print(f"Player loses! {player_hand[0].value} is {str_val} than {dealer_hand[0].value}")
            dealer.award_credits(pot)

        print(f"Player's remaining credits: {player.credits}")
        if player.credits < 10 or dealer.credits < 10:
            print(f"Not enough credits to play again.")
            if player.credits >= 10:
                print("Player Takes the House!")
            else:
                print("You're broke!  Game Over")
            break

        print("Player discards hand")
        discard_pile += player_hand.deal(1)
        print("Dealer discards hand")
        discard_pile += dealer_hand.deal(1)
        print(f"Discard Pile Size {discard_pile.size}")
        if discard_pile.size >= 52:
            print("Last card has been played.  Returning the discard pile to main deck.")
            discard_pile.shuffle()
            deck = discard_pile.deal(52)
            print(f"{deck.size} cards returned from discard pile.")
        print("-----------------------------")
