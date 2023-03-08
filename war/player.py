class Player:
    """Player class."""
    def __init__(self, name, cards, is_player):
        """Player constructor."""
        self.is_player = is_player
        self.name = name
        self.hand = cards
        self.stack = []

    def play_card(self):
        """Pop a card from hand and add to stack."""
        self.stack.append(self.hand.pop(0))

    def add_stack(self, card):
        """Add argument to stack."""
        for c in card:
            self.hand.append(c)

    def get_stack(self):
        """Return stack and clears it."""
        temp_stack = self.stack.copy()
        self.stack.clear()
        return temp_stack

    def stack_empty(self):
        """Return true if stack is empty."""
        return len(self.stack) == 0

    def get_card(self):
        """Return value of latest card added to stack."""
        if len(self.stack) == 0:
            return None

        return self.stack[-1].get_value()

    def hand_empty(self):
        """Return true if hand is empty."""
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
        """Return length of stack."""
        return len(self.stack)

    def len_hand(self):
        """Return length of hand."""
        return len(self.hand)
