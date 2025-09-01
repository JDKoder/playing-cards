import pydealer as pd
from pydealer.const import POKER_RANKS
from player import Player
from rankdicts import HIGH_LOW_RANKS
from card_ascii import print_cards


"""This is a prototype for high_low card game mechanics progress procedurally without user input."""
def run_game():
    #initialize game variables
    round_count = 0
    player_hand = pd.Stack()
    dealer_hand = pd.Stack()
    discard_pile = pd.Stack()
    player = Player(player_hand, 10)
    dealer = Player(dealer_hand, 1000)

    #for i in range(26):
    while True:
        #Round Update phase
        deck = pd.Deck(rebuild=False, re_shuffle=True)
        round_count += 1
        print(f"Round {round_count}")
        for i in range(20):
            deck.shuffle()
        #Draw phase
        #draw a card for the player
        player_hand = deck.deal(1)
        print(f"Players card is {player_hand[0]}")

        def convert_card_to_tuple(card, hidden=False):
            card_tuple = (card.value, card.suit, hidden)
            return card_tuple
        
        def show_hand(hand):
            converted_cards = []
            for i in range(hand.size):
                converted_cards.append(convert_card_to_tuple(hand[i]))
            print_cards(converted_cards)

        player_card_tuple = convert_card_to_tuple(player_hand.cards[0])
        print_cards([player_card_tuple])
        #draw a card for the dealer
        dealer_hand = deck.deal(1)
        print(f"Dealer draws a card face down")
        dealer_card_tuple = convert_card_to_tuple(dealer_hand.cards[0], True)
        print_cards([dealer_card_tuple])

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
        print(f"dealer meets {dealer_wager}")
        pot += dealer.take_credits(dealer_wager)

        #player chooses a to bet "high" or "low"
        player_bet = "high"
        print(f"players bet is {player_bet}")
        print(f"dealer shows their hand")
        print(f"dealer's card is {dealer_hand[0]}")
        show_hand(dealer_hand)

        #whose card is higher
        if player_hand[0].gt(dealer_hand[0], HIGH_LOW_RANKS):
            #player won
            print(f"player wins! {player_hand[0]} is higher than {dealer_hand[0]}")
            print(f"Payout {pot}")
            player.award_credits(pot) 
        elif player_hand[0].eq(dealer_hand[0], HIGH_LOW_RANKS):
            print(f"hands are equal.  That's a push!")
            print(f"Payout {player_wager}")
            player.award_credits(player_wager)
        else:
            print(f"player loses! {player_hand[0]} is lower than {dealer_hand[0]}")
            dealer.award_credits(pot)

        print(f"Player's remaining credits: {player.credits}")
        if player.credits < 10 or dealer.credits < 10:
            print(f"Not enough credits to play again.\n GAME OVER")
            break

        print("Player discards hand")
        discard_pile += player_hand.deal(1)
        print("Dealer discards hand")
        discard_pile += dealer_hand.deal(1)
        print(f"Discard Pile Size {discard_pile.size}")
        if discard_pile.size >= 52:
            print("returning discard pile to main deck")
            discard_pile.shuffle()
            deck = discard_pile.deal(52)
            print(f"{deck.size} cards returned from discard pile.")
        print("-----------------------------")
