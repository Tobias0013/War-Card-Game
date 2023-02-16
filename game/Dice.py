import random


class Dice:
    def __init__(self):
        self.nmr = 0

    def roll(self):
        nmr = random.randint(1, 6)
        return self
