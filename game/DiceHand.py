from game.Dice import Dice


class DiceHand:
    def __init__(self):
        self.dices = []
        self.currentScore = 0

    def rollDice(self):
        dice = Dice.roll()
        if dice.nmr == 1:
            score = 0
        self.currentScore += dice.nmr
        self.dices.add(dice)
        return dice


    def reset(self):
        self.dices.clear()
        self.currentScore = 0
