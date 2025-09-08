from card_ascii import SUIT_ICON, icon_king, icon_queen, icon_jack
from console import console as c
from rich.text import Text
from rich.table import Table

SUIT_STYLE = {
    "Diamonds": "red on white",
    "Hearts": "red on white",
    "Spades": "black on white",
    "Clubs": "black on white",
    "Back": "yellow on black"
}

ICON_RICH_TEXT = {
    "Diamonds": Text(text=SUIT_ICON["Diamonds"], style=SUIT_STYLE["Diamonds"]),
    "Hearts": Text(text=SUIT_ICON["Hearts"], style=SUIT_STYLE["Hearts"]),
    "Spades": Text(text=SUIT_ICON["Spades"], style=SUIT_STYLE["Spades"]),
    "Clubs": Text(text=SUIT_ICON["Clubs"], style=SUIT_STYLE["Clubs"]),
    "King": Text(icon_king),
    "Queen": Text(icon_queen),
    "Jack": Text(icon_jack)
}

RICH_CARD_FACE = {
    "2": """┌──────────┐
│ 2x       │
│          │
│    x     │
│          │
│    x     │
│          │
│       2x │
└──────────┘""",
    "3": """┌──────────┐
│ 3x       │
│          │
│    x     │
│    x     │
│    x     │
│          │
│       3x │
└──────────┘""",
    "4": """┌──────────┐
│ 4x       │
│          │
│  x   x   │
│          │
│  x   x   │
│          │
│       4x │
└──────────┘""",
    "5": """┌──────────┐
│ 5x       │
│          │
│  x   x   │
│    x     │
│  x   x   │
│          │
│       5x │
└──────────┘""",
    "6": """┌──────────┐
│ 6x       │
│          │
│  x   x   │
│  x   x   │
│  x   x   │
│          │
│       6x │
└──────────┘""",
    "7": """┌──────────┐
│ 7x       │
│          │
│  x   x   │
│  x x x   │
│  x   x   │
│          │
│       7x │
└──────────┘""",
    "8": """┌──────────┐
│ 8x       │
│          │
│  x x x   │
│  x x x   │
│  x   x   │
│          │
│       8x │
└──────────┘""",
    "9": """┌──────────┐
│ 9x       │
│          │
│  x x x   │
│  x x x   │
│  x x x   │
│          │
│       9x │
└──────────┘""",
    "10": """┌──────────┐
│ 10x      │
│          │
│  x x x   │
│  x x x   │
│  x x x   │
│    x     │
│      10x │
└──────────┘""",
    "Jack": """┌──────────┐
│ Jx       │
│          │
│          │
│    󰡘     │
│    x     │
│          │
│       Jx │
└──────────┘""",
    "Queen": """┌──────────┐
│ Qx       │
│          │
│          │
│         │
│    x     │
│          │
│       Qx │
└──────────┘""",
    "King": """┌──────────┐
│ Kx       │
│          │
│          │
│    󰆥     │
│    x     │
│          │
│       Kx │
└──────────┘""",
    "Ace": """┌──────────┐
│ Ax       │
│          │
│          │
│    x     │
│          │
│          │
│       Ax │
└──────────┘""",
    "Back": """╔══════════╗
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
║ 󰣏 󰋑 󰣑 󰣎  ║
╚══════════╝"""

}


def convert_face_to_rich_text(card_face_string, suit):
    text_list = []
    last_x_index = 0
    #replace x with icons
    for i in range(len(card_face_string)):
        if card_face_string[i] == "x":
            start_slice = last_x_index
            if(last_x_index > 0):
                start_slice = last_x_index + 1

            text_list.append(Text(text=card_face_string[start_slice:i], style=SUIT_STYLE[suit]))
            text_list.append(ICON_RICH_TEXT[suit])
            last_x_index = i
    #Back card starts from the beginning
    last_slice_start = last_x_index
    if last_x_index > 0:
        last_slice_start += 1
    text_list.append(Text(text=card_face_string[last_slice_start:len(card_face_string)], style=SUIT_STYLE[suit]))
    #test print the list
    face = Text()
    for t in text_list:
        face.append(t)
    return face

CARDS_TABLE_COLUMN_WIDTH = 13

def convert_rich_cards_to_grid(rich_markup):
    grid = Table.grid()
    for i in rich_markup:
        grid.add_column(width=CARDS_TABLE_COLUMN_WIDTH)
    grid.add_row(*rich_markup)
    return grid

"""rich_faces = []
rich_faces.append(convert_face_to_rich_text(RICH_CARD_FACE["10"], "Clubs"))
rich_faces.append(convert_face_to_rich_text(RICH_CARD_FACE["Ace"], "Hearts"))
grid = convert_rich_cards_to_grid(rich_faces)
c.print(grid)"""

