HIGH_LOW_RANKS = { 
        "Ace High": 13,
        "King": 12,
        "Queen": 11,
        "Jack": 10,
        "10": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "Ace Low": 0,
}

BLACKJACK_RANKS = { 
        "Ace": 11,
        "King": 10,
        "Queen": 10,
        "Jack": 10,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
}

WAR_RANKS = { 
        "Ace": 14,
        "King": 13,
        "Queen": 12,
        "Jack": 11,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
}

def card_to_int(card,rank_dict) -> int:
    return rank_dict[card.value]

def stack_to_int(stack,rank_dict) -> int:
    accumulator = 0
    for card in stack:
        accumulator += card_to_int(card, rank_dict)
    return accumulator


