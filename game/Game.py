from HighScore import High_score
from Deck import Deck
import operator
import pickle


class Game:
    def __init__(self):
        self._path = "highScore.bin"
        self.high_scores = [High_score]
        self.round_counter = int()
        self.deck = Deck()
        self.player1 = None #player class
        self.player2 = None #player class

    def start(self):
        return

    def end(self):
        return

    def _load_high_score(self):
        with open(self._path, "rb") as file:
            return pickle.load(file)

    def _save_high_score(self, high_scores):
        with open(self._path, "wb") as file:
            pickle.dump(self.high_scores, file)

    def _copare_high_scores(self):
        self.high_scores.sort(key=operator.attrgetter("rounds"))

        while len(self.high_scores > 5):
            del self.high_scores[5]

