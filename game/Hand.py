class Hand:
    def __init__(self, hand):
        self.hand = hand

    def add_card(self, cards):
        while len(cards) != 0:
            self.hand.append(cards.pop())
    
    def get_next_card(self):
        return self.hand.pop(0)

    def remove_card(self):
        self.hand.get()