from enum import Enum
class PlayingCard():

    def __init__(self, face_value, suit):
        self.face_value = face_value
        self.suit = suit

    def __repr__(self):
        return f"{self.face_value} of {self.suit}"

    def compare(self, other):
        if other.face_value == self.face_value:
            return 0
        elif other.face_value > self.face_value:
            return -1
        else:
            return 1

class suits(Enum):
    HEARTS
    DIAMONDS
    SPADES
    CLUBS

class face_value(Enum):
    A
    2
    3
    4
    5
    6
    7
    8
    9
    10
    J
    Q
    K
