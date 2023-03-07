
"""Game class."""

import operator
import pickle
from war import high_score
from war import deck
from war import player
from war import card


class Game:
    """Game class."""
    def __init__(self):
        """Game constructor."""
        self._path = "highScore.bin"
        self.round_counter = int()
        self.deck = deck.Deck()
        self.high_scores = []
        self.high_scores = self.load_high_score()
        self.player1 = None
        self.player2 = None

    def start(self, name1, name2, is_player):
        """Game start."""
        hand1 = []
        hand2 = []
        self.deck.give_hands(hand1, hand2)
        self.player1 = player.Player(name1, hand1, True)
        self.player2 = player.Player(name2, hand2, is_player)

    def end(self):
        """Game end."""
        end = False

        if self.player1.stack_empty() and self.player2.stack_empty():
            # checks if player1 hand is empty
            if self.player1.hand_empty():
                print("player 2 won")
                end = True
                self._create_high_score(self.player2, self.player1)
            # checks if player2 hand is empty
            elif self.player2.hand_empty():
                print("player 1 won")
                end = True
                self._create_high_score(self.player1, self.player2)

        return end

    def _create_high_score(self, player_winner, player_looser):
        """Creates high score."""
        high = high_score.High_score(self.round_counter, player_winner, player_looser)
        self.high_scores.append(high)
        self._compare_high_scores()
        self._save_high_score()

    def load_high_score(self):
        """Load high scores."""
        try:
            with open(self._path, "rb") as file:
                return pickle.load(file)
        except:
            return []

    def _save_high_score(self):
        """Save high scores."""
        if self._path == "":
            return

        with open(self._path, "wb") as file:
            pickle.dump(self.high_scores, file)

    def _compare_high_scores(self):
        """Compares high scores and keeps 5 highest."""
        self.high_scores.sort(key=operator.attrgetter("rounds"))

        while len(self.high_scores) > 5:
            del self.high_scores[5]

    def compare_cards(self):
        """Compare cards."""
        # if both stacks have card in them check witch is bigger than give both card to that player
        if not self.player1.stack_empty() and not self.player2.stack_empty():
            # This checks if player1 card has higher value
            if self.player1.get_card() > self.player2.get_card():
                print("Player1 has higher card")
                print(f"Player1 card: {self.player1.get_card()}")
                print(f"Player2 card: {self.player2.get_card()}")
                self.player1.add_stack(self.player1.get_stack())
                self.player1.add_stack(self.player2.get_stack())
                print(
                    f"Player1 hand len: {self.player1.len_hand()} Player2 hand len: {self.player2.len_hand()}"
                )
                self.round_counter += 1
            # This checks if player2 card has higher value
            elif self.player2.get_card() > self.player1.get_card():
                print("Player2 has higher card")
                print(f"Player1 card: {self.player1.get_card()}")
                print(f"Player2 card: {self.player2.get_card()}")
                self.player2.add_stack(self.player1.get_stack())
                self.player2.add_stack(self.player2.get_stack())
                print(
                    f"Player1 hand len: {self.player1.len_hand()} Player2 hand len: {self.player2.len_hand()}"
                )
                self.round_counter += 1
            # this hapends if both players card have same value
            else:
                # plays 2 cards from each hand
                self.player1.play_card()
                self.player1.play_card()
                self.player2.play_card()
                self.player2.play_card()
                print("Both players have same value")
                print(f"Player1 card: {self.player1.get_card()}")
                print(f"Player2 card: {self.player2.get_card()}")
                print(
                    f"Player1 hand len: {self.player1.len_hand()} Player2 hand len: {self.player2.len_hand()}"
                )
                self.compare_cards()

    def cheat(self):
        """Cheat, riggs war so that player 1 will win."""
        self.player1.clear_stack()
        self.player1.clear_hand()
        self.player2.clear_stack()
        self.player2.clear_hand()
        self.player1.hand.append(card.Card(14, 0))
        self.player2.hand.append(card.Card(2, 0))
