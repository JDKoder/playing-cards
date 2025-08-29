import pydealer as pd
from pydealer.const import POKER_RANKS
from player import Player
from rankdicts import HIGH_LOW_RANKS


"""This is a prototype for high_low card game mechanics progress procedurally without user input."""
def run_game():
    #create the game deck preshuffled
    deck = pd.Deck(rebuild=False, re_shuffle=True)
    round_count = 0
    #Draw phase
    #Create a player and a dealer that get 1 card each

    for i in range(26):
        round_count += 1
        print(f"Round {round_count}")
        deck.shuffle()
        #draw a card for the player
        player_hand = deck.deal(1)
        print(f"Players card is {player_hand[0]}")
        #draw a card for the dealer
        dealer_hand = deck.deal(1)

        player = Player(player_hand, 10)
        dealer = Player(dealer_hand, 1000)

        #Wager phase
        # player chooses the wager and the dealer matches, all credits go into the pot
        # if the dealer can't match, the wager must be the maximum left in the dealers account and the 
        # remainder is returned to the player's credits
        player_wager = 10
        dealer_wager = player_wager
        pot = 0
        if dealer.credits < player_wager:
            print(f"dealer will match up to {dealer.credits}")
            player_wager = dealer.credits
            dealer_wager = dealer.credits

        # Finalize Bet phase
        print(f"player wagers {player_wager}")
        pot += player.take_credits(player_wager)
        print(f"dealer wagers {dealer_wager}")
        pot += dealer.take_credits(dealer_wager)

        #player chooses a to bet "high" or "low"
        player_bet = "high"
        print(f"players bet is {player_bet}")
        print(f"dealers card is {dealer.hand[0]}")
        #whose card is higher
        if player.hand[0].gt(dealer.hand[0], HIGH_LOW_RANKS):
            #player won
            print(f"player wins! {player.hand[0]} is higher than {dealer.hand[0]}")
            print(f"Payout {pot}")
            player.award_credits(pot) 
        elif player.hand[0].eq(dealer.hand[0], HIGH_LOW_RANKS):
            print(f"hands are equal.  That's a push!")
            print(f"Payout {player_wager}")
            player.award_credits(player_wager)
        else:
            print(f"player loses! {player.hand[0]} is lower than {dealer.hand[0]}")
            dealer.award_credits(pot)

        print(f"Player's remaining credits: {player.credits}")
        if player.credits < 10:
            print(f"Not enough credits to play again.\n GAME OVER")
            break
        print("-----------------------------")
