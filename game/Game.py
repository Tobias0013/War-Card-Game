from HighScore import High_score
from Deck import Deck
import operator
import pickle
import Player


class Game:
    def __init__(self):
        self._path = "highScore.bin"
        self.high_scores = [High_score]
        self.round_counter = int()
        self.deck = Deck()

    def start(self, name1, name2, is_player ):
        hand1 = list()
        hand2 = list()
        self.deck.give_hands(hand1, hand2)
        self.player1 = Player.Player(name1, hand1, True)
        self.player2 = Player.Player(name2, hand2, is_player)

    def end(self):
        # checks if player1 hand is empty
        if len(self.player1.stack) != 0 or len(self.player2.stack) != 0:
            return False

        if len(self.player1.hand) == 0:
            print("player 2 won")

        # checks if player2 hand is empty
        elif len(self.player2.hand) == 0:
            print("player 1 won")

        #save high score osv.
        return True

    def _load_high_score(self):
        with open(self._path, "rb") as file:
            self.high_scores = pickle.load(file)

    def _save_high_score(self, high_scores):
        with open(self._path, "wb") as file:
            pickle.dump(self.high_scores, file)

    def _compare_high_scores(self):
        self.high_scores.sort(key=operator.attrgetter("rounds"))

        while len(self.high_scores > 5):
            del self.high_scores[5]

