from rankdicts import WAR_RANKS



#Alright, now we need to know what the favorable outcomes are.
#First What's our cards value
first_card_value = 3
print(f"hand1 value {first_card_value}")
#How many cards are less than this card
cards_that_beat_player = 0
cards_that_player_beats = 0
for rank in WAR_RANKS:
    print(f"does {first_card_value} beat {WAR_RANKS[rank]}")
    if first_card_value > WAR_RANKS[rank]:
        cards_that_player_beats += 4
    elif first_card_value == WAR_RANKS[rank]:
        cards_that_player_beats += 3
    else:
        cards_that_beat_player += 4

print(f"cards that beat player {cards_that_beat_player}")
print(f"cards that player beats {cards_that_player_beats}")

