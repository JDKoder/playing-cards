import unittest
from card import PlayingCard
from player import Player

class TestPlayer(unittest.TestCase):

    def test_player_repr(self):
        player = Player([PlayingCard("2", "hearts"),PlayingCard("3", "spades"), PlayingCard("4", "diamonds")], 10)
        self.assertEqual("Player has 3 cards and 10 credits", str(player))

    def test_take_credits(self):
        player = Player([PlayingCard("2", "hearts"),PlayingCard("3", "spades"), PlayingCard("4", "diamonds")], 10)
        player.take_credits(5)
        self.assertEqual("Player has 3 cards and 5 credits", str(player))

    def test_take_credits_too_many(self):
        player = Player([PlayingCard("2", "hearts"),PlayingCard("3", "spades"), PlayingCard("4", "diamonds")], 10)
        try:
            player.take_credits(59)
            self.fail("Taking more credits than player has should throw a ValueError")
        except ValueError:
            pass

    def test_add_card_to_hand(self):
        player = Player([PlayingCard("2", "hearts"),PlayingCard("3", "spades"), PlayingCard("4", "diamonds")], 10)
        player.add_card_to_hand(PlayingCard("5", "clubs"))
        self.assertEqual("Player has 4 cards and 10 credits", str(player))

    def test_award_credits(self):
        player = Player([PlayingCard("2", "hearts"),PlayingCard("3", "spades"), PlayingCard("4", "diamonds")], 10)
        player.award_credits(10)
        self.assertEqual("Player has 3 cards and 20 credits", str(player))
