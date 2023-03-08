"""
When executing, it creates 2 players and a hand for each player. It also determines 
if player 2 is a computer or a player.

        def start(self, name1, name2, is_player):

If both player stacks are empty.
Then checks if either player has a empty hand. 
If so then the other player wins. Then creates a high score.

        def end(self):
        
Checks if both stacks is not empty. Then checks if either player has a higher card value.
The player with the higher card value will win that round thus recieving all the played cards from both players.

If both of the players card have the same value, then playes two more cards from each player 
and then runs compare_cards() again.

        def compare_cards(self):

"""

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
        """Start the game."""
        hand1 = []
        hand2 = []
        self.deck.give_hands(hand1, hand2)
        self.player1 = player.Player(name1, hand1, True)
        self.player2 = player.Player(name2, hand2, is_player)

    def end(self):
        """Checks if game should end."""
        end = False

        if self.player1.stack_empty() and self.player2.stack_empty():
            if self.player1.hand_empty():
                print("player 2 won")
                end = True
                self._create_high_score(self.player2, self.player1)
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
        """Load high scores from file."""
        if self._path == "":
            return
        
        try:
            with open(self._path, "rb") as file:
                return pickle.load(file)
        except:
            return []

    def _save_high_score(self):
        """Save high scores to file."""
        if self._path == "":
            return

        with open(self._path, "wb") as file:
            pickle.dump(self.high_scores, file)

    def _compare_high_scores(self):
        """Compares high scores and keeps 5 highest."""
        
        #Sort list by variable rounds. Lowest first. 
        self.high_scores.sort(key=operator.attrgetter("rounds"))

        while len(self.high_scores) > 5:
            del self.high_scores[5]

    def compare_cards(self):
        """Compare cards, and give cards to player with highest card value."""
        if not self.player1.stack_empty() and not self.player2.stack_empty():
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
            else:
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
