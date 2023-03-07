#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

from unittest import mock
import unittest
import pickle
from war import game
from war import player
from war import card
from war import high_score


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = game.Game()
        exp = game.Game
        self.assertIsInstance(res, exp)

    def test_start(self):
        """Test start game."""
        the_game = game.Game()
        the_game.start("Karl", "Markus", True)

        self.assertIsNotNone(the_game.player1)
        self.assertIsNotNone(the_game.player2)

        self.assertIsInstance(the_game.player1, player.Player)
        self.assertIsInstance(the_game.player2, player.Player)

        res = len(the_game.player1.hand) == 26
        self.assertTrue(res)
        res = len(the_game.player2.hand) == 26
        self.assertTrue(res)

        self.assertIsInstance(the_game.player1.hand[0], card.Card)
        self.assertIsInstance(the_game.player2.hand[0], card.Card)

    def test_compare_cards(self):
        """Test compare cards."""
        the_game = game.Game()
        the_game.start("player1", "player2", False)

        # Player 2 win
        the_game.player1.clear_hand()
        the_game.player2.clear_hand()
        the_game.player1.stack.append(card.Card(2, 0))
        the_game.player2.stack.append(card.Card(14, 0))
        res = the_game.player1.len_stack() == 1 and the_game.player2.len_stack() == 1
        self.assertTrue(res)

        the_game.compare_cards()
        res = the_game.player2.len_hand() == 2 and the_game.player1.hand_empty()
        self.assertTrue(res)

        # Player 1 win
        the_game.player1.clear_hand()
        the_game.player2.clear_hand()
        the_game.player1.stack.append(card.Card(14, 0))
        the_game.player2.stack.append(card.Card(2, 0))
        res = the_game.player1.len_stack() == 1 and the_game.player2.len_stack() == 1
        self.assertTrue(res)

        the_game.compare_cards()
        res = the_game.player2.hand_empty() and the_game.player1.len_hand() == 2
        self.assertTrue(res)

        # Player same vale then player 1 win
        the_game.player1.clear_hand()
        the_game.player2.clear_hand()

        the_game.player1.stack.append(card.Card(8, 0))
        the_game.player1.hand.append(card.Card(10, 0))
        the_game.player1.hand.append(card.Card(14, 0))

        the_game.player2.stack.append(card.Card(8, 0))
        the_game.player2.hand.append(card.Card(7, 0))
        the_game.player2.hand.append(card.Card(2, 0))

        res = the_game.player1.len_stack() == 1 and the_game.player2.len_stack() == 1
        self.assertTrue(res)
        res = the_game.player1.len_hand() == 2 and the_game.player2.len_hand() == 2
        self.assertTrue(res)

        the_game.compare_cards()
        res = the_game.player2.hand_empty() and the_game.player1.len_hand() == 6
        self.assertTrue(res)

    def test_save_high_score(self):
        """Test save high score."""
        self._clear_file()
        the_game = game.Game()
        the_game._path = "test/highScore.bin"
        p1 = player.Player("p1", [], True)
        p2 = player.Player("p2", [], True)
        temp_list = [high_score.High_score(0, p1, p2)]
        the_game.high_scores = temp_list
        the_game._save_high_score()

        res = self._read_file() == temp_list
        self.assertTrue(res)

    def test_compare_high_scores(self):
        """Test compare high scores."""
        the_game = game.Game()
        the_game.high_scores.clear()
        p1 = player.Player("p1", [], True)
        p2 = player.Player("p2", [], True)
        high_scores = [high_score.High_score(10, p1, p2),
                       high_score.High_score(20, p1, p2),
                       high_score.High_score(5, p1, p2),
                       high_score.High_score(3, p1, p2),
                       high_score.High_score(7, p1, p2),
                       high_score.High_score(1, p1, p2)]
        the_game.high_scores = high_scores
        the_game._compare_high_scores()
        high_scores = [high_score.High_score(1, p1, p2),
                       high_score.High_score(3, p1, p2),
                       high_score.High_score(5, p1, p2),
                       high_score.High_score(7, p1, p2),
                       high_score.High_score(10, p1, p2)]
        res = the_game.high_scores == high_scores
        self.assertTrue(res)

    def test_create_high_score(self):
        """Test create high score."""
        the_game = game.Game()
        the_game.high_scores.clear()
        the_game._path = ""
        the_game.round_counter = 0
        p1 = player.Player("p1", [], True)
        p2 = player.Player("p2", [], True)
        the_game._create_high_score(p1, p2)
        res = the_game.high_scores
        temp_list = [high_score.High_score(0, p1, p2)]
        exp = temp_list
        self.assertEqual(res, exp)

    def test_load_high_score(self):
        """Test load high score."""
        the_game = game.Game()
        the_game.high_scores.clear()
        the_game._path = "test/highScore.bin"
        the_game.high_scores = the_game.load_high_score()
        res = the_game.high_scores
        exp = self._read_file()
        self.assertEqual(res, exp)

    def test_cheat(self):
        """Test chet."""
        the_game = game.Game()
        the_game.player1 = player.Player("p1", [], True)
        the_game.player2 = player.Player("p2", [], True)
        the_game.cheat()
        res = the_game.player1.len_hand() == 1 \
              and the_game.player2.len_hand() == 1
        self.assertTrue(res)

        res = the_game.player1.hand[0].get_value() == 14
        self.assertTrue(res)

        res = the_game.player2.hand[0].get_value() == 2
        self.assertTrue(res)

    def test_end(self):
        """Test end game."""
        the_game = game.Game()
        the_game._path = ""
        the_game.start("Karl", "Markus", True)

        self.assertFalse(the_game.end())

        the_game.player1.clear_hand()
        self.assertTrue(the_game.end())

        the_game.start("Karl", "Markus", True)
        the_game.player2.clear_hand()
        self.assertTrue(the_game.end())

        the_game.start("Karl", "Markus", True)
        the_game.player1.clear_hand()
        the_game.player2.clear_hand()
        self.assertTrue(the_game.end())

    def _clear_file(self):
        """Clear test/highScore.bin file."""
        open("test/highScore.bin", "w").close()

    def _read_file(self):
        """Read test/highScore.bin file. Return a list of high scores."""
        try:
            with open("test/highScore.bin", "rb") as file:
                return pickle.load(file)
        except:
            return []


if __name__ == "__main__":
    unittest.main()
