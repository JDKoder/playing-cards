from pydealer import Stack

class Player():

    def __init__(self, hand=[], credits=0):
        self.hand = hand
        self.credits = credits


    def __repr__(self):
        return f"Player has {len(self.hand)} cards and {self.credits} credits"

    def take_credits(self, amount):
        if amount > self.credits:
            raise ValueError("Player does not have enough credits")
        self.credits -= amount
        return amount

    def award_credits(self, amount):
        self.credits += amount

    """Adds a card to the top of the given players hand."""
    def add_card_to_hand(self, card):
        if type(self.hand) is Stack:
            self.hand.add(card)
        else:
            self.hand.append(card)



