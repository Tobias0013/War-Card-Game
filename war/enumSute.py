"""EnumSute file."""


from enum import Enum


class Sute(Enum):
    """Enum for card sute."""

    HEARTS = 0
    DIAMONDS = 1
    SPADES = 2
    CLUBS = 3
