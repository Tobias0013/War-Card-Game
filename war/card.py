
"""Card class."""

from war.enumNumber import number
from war.enumColor import Color
from war.enumSute import Sute


class Card:
    """Card class."""
    def __init__(self, nmr, suite):
        """Card constructor."""
        self.number = number(nmr)
        if suite in (0, 1):
            self.color = Color.RED
        else:
            self.color = Color.BLACK
        self.suite = Sute(suite)

    def get_value(self):
        """Gets the cards value(number on the card)."""
        return self.number.value

    def __str__(self):
        """To string method."""
        return f"number={self.number.value},suite={self.suite},color={self.color}"
