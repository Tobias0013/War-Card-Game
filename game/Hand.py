from queue import LifoQueue

class Hand:
    def __init__(self, cards):
        self.hand = LifoQueue()
        while cards.not_empty():
            self.hand.put(cards.get())

    def next_card(self):
        return self.hand.get()

    def add_card(self, card):
        self.hand.put(card)

    def remove_card(self):
        self.hand.get()