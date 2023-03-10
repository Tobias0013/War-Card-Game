"""Card file."""

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
        """Get the card value."""
        return self.number.value

    def __str__(self):
        """Return card as string."""
        return f"number={self.number.value}," + \
            f"suite={self.suite},color={self.color}"
