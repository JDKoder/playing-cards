from card_ascii import print_cards, print_card, CARD_FACE, SUIT_ICON


def test_print():
    for rank in CARD_FACE.keys():
        for suit in SUIT_ICON.keys():
            is_back = False
            if rank == "Back":
                is_back = True
            print_card(rank, suit, is_back)


test_print()
print_cards([("Ace", "Spades", False),("10","Clubs", False),("King", "Diamonds", True)])
