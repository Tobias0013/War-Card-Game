from Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = list()
        self._generate_cards()
        random.shuffle(self.cards)

    def _generate_cards(self):
        i = 0
        j = 0

        while i < 13:
            while j < 4:
                self.cards.append(Card(i, j))
                j += 1
            j = 0
            i += 1

    def give_hands(self, hand1=[], hand2=[]):
        for i, card in enumerate(self.cards):
            if i % 2 == 0:
                hand1.append(card)
            else:
                hand2.append(card)
