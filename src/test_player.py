import unittest
from player import Player
import pydealer as pd

class TestPlayer(unittest.TestCase):

    def setup_player(self):
        player_hand = pd.Stack()
        deck = pd.Deck()
        player_hand += deck.deal(3)
        player = Player(player_hand, 10) 
        return player

    def test_player_repr(self):
        player = self.setup_player()
        self.assertEqual("Player has 3 cards and 10 credits", str(player))

    def test_take_credits(self):
        player = self.setup_player()
        player.take_credits(5)
        self.assertEqual("Player has 3 cards and 5 credits", str(player))

    def test_take_credits_too_many(self):
        player = self.setup_player()
        try:
            player.take_credits(59)
            self.fail("Taking more credits than player has should throw a ValueError")
        except ValueError:
            pass

    def test_add_card_to_hand(self):
        player = self.setup_player()
        player.add_card_to_hand(pd.Deck().deal(1))
        self.assertEqual("Player has 4 cards and 10 credits", str(player))

    def test_award_credits(self):
        player = self.setup_player()
        player.award_credits(10)
        self.assertEqual("Player has 3 cards and 20 credits", str(player))
