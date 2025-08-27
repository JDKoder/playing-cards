import pydealer as pd
from player import Player

"""This is a prototype for how the game mechanics progress basically."""
def main():
    #create the game deck preshuffled
    deck = pd.Deck(rebuild=True, re_shuffle=True)
    #draw a card for the player
    player_hand = deck.deal(1)
    #draw a card for the dealer
    dealer_hand = deck.deal(1)
    #Draw phase
    #Create a player and a dealer that get 1 card each


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

    pot += player.take_credits(player_wager)
    pot += dealer.take_credits(dealer_wager)

    #player chooses a to bet "high" or "low"
    player_bet = "high"

    #whose card is higher
    if player.hand[0] > dealer.hand[0]:
        #player won
        print(f"player wins! {player.hand[0]} is higher than {dealer.hand[0]}")
        print(f"Payout {pot}")
        player.award_credits(pot) 
    elif player.hand[0] == dealer.hand[0]:
        print(f"hand are equal.  That's a push!")
        print(f"Payout {player_wager}")
        player.award_credits(player_wager)
    else:
        print(f"player loses! {player.hand[0]} is lower than {dealer.hand[0]}")
        dealer.award_credits(pot)

main()
