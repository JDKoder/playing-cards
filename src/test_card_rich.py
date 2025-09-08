from card_rich import RICH_CARD_FACE, convert_face_to_rich_text, convert_rich_cards_to_grid
from console import console as c

rich_faces = []
rich_faces.append(convert_face_to_rich_text(RICH_CARD_FACE["10"], "Clubs"))
rich_faces.append(convert_face_to_rich_text(RICH_CARD_FACE["Ace"], "Hearts"))
grid = convert_rich_cards_to_grid(rich_faces)
c.print(grid)
