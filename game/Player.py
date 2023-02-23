from queue import LifoQueue
import Hand

class Player:
    def __init__(self, name, cards):
        obj = Hand.Hand(cards)
        self.name = name
        self.current_cards = obj.hand

    def play_hand(self):
        if self.current_cards.not_empty() == False:
            print("The deck is empty")              #Needed change: a signal that the player has lost
        else:
            print(f'{self.name} plays >> {self.current_cards.get()}')

    def change_name(self):
        self.name = input('What is your new name? >> ')

    def add_cards(self, cards):
        while cards.not_empty():
            self.current_cards.put(cards.pop())