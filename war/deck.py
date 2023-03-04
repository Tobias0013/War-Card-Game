
"""Deck class."""

import random
from war import card


class Deck:
    """Deck class."""
    def __init__(self):
        """Deck constructor."""
        self.cards = []
        self._generate_cards()
        random.shuffle(self.cards)

    def _generate_cards(self):
        """Generates card."""
        i = 2
        j = 0

        while i < 15:
            while j < 4:
                self.cards.append(card.Card(i, j))
                j += 1
            j = 0
            i += 1

    def give_hands(self, hand1, hand2):
        for i, card in enumerate(self.cards):
            if i % 2 == 0:
                hand1.append(card)
            else:
                hand2.append(card)
