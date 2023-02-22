from queue import LifoQueue
import Game

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = LifoQueue()

        while hand.not_empty():
            self.hand.put(hand.get())

    def main(self):
        try:
            enter = input('Press enter to play next card (type "change" for name change) \n >> ')
            if enter == 'change':
                self.change_name()
        except(TypeError):
            print('Please press a valid input')
        self.play_card()

    def play_card(self):
        if self.current_cards.not_empty() == False:
            print("The deck is empty")              #Needed change: a signal that the player has lost
        else:
            print(f'{self.name} plays >> {self.current_cards.get}')

    def change_name(self):
        self.name = input('What is your new name? >> ')

    def add_cards(self, cards):
        while cards.not_empty():
            self.hand.put(cards.get())

    if __name__ == '__main__':
        main()