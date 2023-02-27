import Hand
from Card import Card

class Player:
    def __init__(self, name, cards, is_player):
        self.is_player = is_player
        self.name = name
        self.hand = cards
        self.stack = []

    def play_card(self):
        self.stack.append(self.hand.pop(0))

    def add_stack(self, card):
        for c in card:
            self.hand.append(c)

    def get_stack(self):
        temp_stack = self.stack.copy()
        self.stack.clear()
        return temp_stack
    
    def change_name(self):
        self.name = input('What is your new name? >> ')
        