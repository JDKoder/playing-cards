from card_ascii import SUIT_STYLE, ICON_RICH_TEXT, SUIT_ICON, CARD_FACE
from rich.console import Console
from rich.text import Text

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
│          │
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
console = Console()
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
    text_list.append(Text(text=card_face_string[last_x_index + 1:len(card_face_string)], style=SUIT_STYLE[suit]))
    #test print the list
    face = Text()
    for t in text_list:
        face.append(t)
    return face

card_face_string = """            
     x      
            
     x      
            """

console.print(convert_face_to_rich_text(RICH_CARD_FACE["10"], "Diamonds"))
console.print(Text(text="foobarbaz"))
