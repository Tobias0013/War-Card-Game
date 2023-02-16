from game.DiceHand import DiceHand


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.diceHand = DiceHand()

    def _addScore(self, score):
        return

    def turn(self):
        print(f"it is now {self.name}s turn")
        dice = self.diceHand.rollDice()
        print(f"{self.name} rolled a {dice.nmr}")
        if dice.nmr == 1:
            return "avslut"


