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
        """Returns stack and clears it."""
        temp_stack = self.stack.copy()
        self.stack.clear()
        return temp_stack

    def stack_empty(self):
        """Checks if stack is empty."""
        return len(self.stack) == 0

    def get_card(self):
        """Returns latest card added to stack."""
        if len(self.stack) == 0:
            return None

        return self.stack[-1].get_value()

    def hand_empty(self):
        """Checks if hand is empty."""
        return len(self.hand) == 0

    def clear_stack(self):
        """Clears stack."""
        self.stack.clear()

    def clear_hand(self):
        """Clears hand."""
        self.hand.clear()

    def change_name(self):
        """Changes name of player."""
        self.name = input("What is your new name? >> ")

    def len_stack(self):
        """Retrunrs legth of stack."""
        return len(self.stack)

    def len_hand(self):
        """Retrunrs legth of hand."""
        return len(self.hand)
