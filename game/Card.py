from EnumNumber import Number
from EnumColor import Color
from EnumSute import Sute


class Card:
    def __init__(self, number=int(), suite=int()):
        self.number = Number(number)
        if suite == 0 or suite == 1:
            self.color = Color.Red
        else:
            self.color = Color.Black
        self.suite = Sute(suite)

    def __str__(self):
        return f"number={self.number.value},suite={self.suite},color={self.color}"
