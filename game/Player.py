from queue import LifoQueue
import Hand

class Player:
    def __init__(self, name, cards, is_player):
        self.is_player = is_player
        self.name = name
        self.current_cards = Hand.Hand(cards).hand

    def play_hand(self):
        if self.current_cards.not_empty() == False:
            print("The deck is empty")
        else:
            print(f'{self.name} plays >> {self.current_cards.get()}')

    def change_name(self):
        self.name = input('What is your new name? >> ')

    def add_cards(self, cards):
        while cards.not_empty():
            self.current_cards.put(cards.pop())