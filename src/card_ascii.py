icon_spade = "󰣑"
icon_club = "󰣎"
icon_heart = "󰋑"
icon_diamond = "󰣏"
icon_queen = ""
icon_jack = "󰡘"
icon_king = "󰆥"

SUIT_ICON = {
    "Diamonds":"󰣏",
    "Hearts":"󰋑",
    "Spades":"󰣑",
    "Clubs":"󰣎"
}

CARD_FACE = {
    "2": """│          │
│    x     │
│          │
│    x     │
│          │""",
    "3": """│          │
│    x     │
│    x     │
│    x     │
│          │""",
    "4": """│          │
│  x   x   │
│          │
│  x   x   │
│          │""",
    "5": """│          │
│  x   x   │
│    x     │
│  x   x   │
│          │""",
    "6": """│          │
│  x   x   │
│  x   x   │
│  x   x   │
│          │""",
    "7": """│          │
│  x   x   │
│  x x x   │
│  x   x   │
│          │""",
    "8": """│          │
│  x x x   │
│  x x x   │
│  x   x   │
│          │""",
    "9": """│          │
│  x x x   │
│  x x x   │
│  x x x   │
│          │""",
    "10": """│          │
│  x x x   │
│  x x x   │
│  x x x   │
│    x     │""",
    "Jack": """│          │
│          │
│    󰡘     │
│    x     │
│          │""",
    "Queen": """│          │
│          │
│         │
│    x     │
│          │""",
    "King": """│          │
│          │
│    󰆥     │
│    x     │
│          │""",
    "Ace": """│          │
│          │
│    x     │
│          │
│          │""",
    "Back": """║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║"""

}

card_top = f"┌──────────┐"
card_bottom = f"└──────────┘"

card_back_top = f"╔══════════╗"
card_back_bottom = f"╚══════════╝"

#todo: build back of card
def build_card_string(value, suit):
    icon = SUIT_ICON[suit]
    face = CARD_FACE[value]
    face = face.replace("x", icon)
    rank = value
    card_str = ""
    #face cards should only display J, Q, K as their rank
    if value in ["Jack","Queen","King","Ace"]:
        rank = value[0:1]

    if value == "Back":
        card_str += f"{card_back_top}\n"
    else:
        card_str += f"{card_top}\n"

    if value == "10":
        card_str += f"│ {rank}{icon}      │\n"
    elif value == "Back":
        card_str += f"║ 󰣏 󰋑 󰣑 󰣎  ║\n"
    else:
        card_str += f"│ {rank}{icon}       │\n"

    card_str += f"{face}\n"

    if value == "10":
        card_str += f"│      {rank}{icon} │\n"
    elif value == "Back":
        card_str += f"║ 󰣏 󰋑 󰣑 󰣎  ║\n"
    else:
        card_str += f"│       {rank}{icon} │\n"

    if value == "Back":
        card_str += card_back_bottom
    else:
        card_str += card_bottom
    return card_str


def print_card(value, suit):
    card_string = build_card_string(value, suit)
    print(card_string)

CARD_WIDTH=12
CARD_HEIGHT=9
#takes a list of cards (tuples with value, and suit) and prints them side by side
def print_cards(cards):
    #build cards strings and put them in a list
    card_strings = []
    for card in cards:
        card_strings.append(build_card_string(card[0], card[1]))

    for row in range(CARD_HEIGHT):
        line_str = ""
        for card_string in card_strings:
            cursor_pos = row * CARD_WIDTH + row
            line_str += card_string[cursor_pos:cursor_pos+CARD_WIDTH]
        print(line_str)

def test_print():
    for rank in CARD_FACE.keys():
        for suit in SUIT_ICON.keys():
            print_card(rank, suit)


test_print()
print_cards([("Ace", "Spades"),("10","Clubs")])
