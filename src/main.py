import pydealer as pd
from pydealer.const import POKER_RANKS
from player import Player

HIGH_LOW_RANKS = { 
        "2": 13,
        "Ace": 12,
        "King": 11,
        "Queen": 10,
        "Jack": 9,
        "10": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
        "Joker": 0
}

"""This is a prototype for how the game mechanics progress basically."""
def main():
    #create the game deck preshuffled
    deck = pd.Deck(rebuild=True, re_shuffle=True)
    #Draw phase
    #Create a player and a dealer that get 1 card each

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
        print(f"hand are equal.  That's a push!")
        print(f"Payout {player_wager}")
        player.award_credits(player_wager)
    else:
        print(f"player loses! {player.hand[0]} is lower than {dealer.hand[0]}")
        dealer.award_credits(pot)

main()
