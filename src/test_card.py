import unittest
from card import PlayingCard

class PlayingCardTest(unittest.TestCase):
    def test_repr(self):
        card_2_of_hearts = PlayingCard("2", "hearts")
        self.assertEqual("2 of hearts", str(card_2_of_hearts))
