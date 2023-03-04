
"""Class hand."""


class Hand:
    """Class hand."""

    def __init__(self, hand):
        """Hand constructor."""
        self.hand = hand

    def add_card(self, cards):
        """Add card."""
        while len(cards) != 0:
            self.hand.append(cards.pop())

    def get_next_card(self):
        """Get next card."""
        return self.hand.pop(0)

    def remove_card(self):
        """Remove card."""
        self.hand.get()
