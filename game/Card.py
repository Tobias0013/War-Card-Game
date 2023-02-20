from EnumNumber import Number
from EnumColor import Color
from EnumSute import Sute


class Card:
    def __init__(self, number=int(), suite=int()):
        self.number = self._int_to_number(number)
        if suite == 0 or suite == 1:
            self.color = Color.Red
        else:
            self.color = Color.Black
        self.suite = self._int_to_suite(suite)

    @staticmethod
    def _int_to_number(nmr=int()):
        return Number(nmr)

    @staticmethod
    def _int_to_suite(nmr=int()):
        return Sute(nmr)

    def __str__(self):
        return f"number={self.number.value},suite={self.suite},color={self.color}"
