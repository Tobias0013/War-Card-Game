#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from war import game
from war import card


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties"""
        res = game.Game()
        self.assertIsInstance(res, game.Game)

        self.assertTrue(len(res.high_scores) != 0)
        self.assertIsInstance(res.round_counter, int)

    def test_start_the_game(self):
        """Check if start() creates 2 players with a hand"""
        the_game = game.Game()
        the_game.start("Karl", "Markus", True)

        self.assertIsNotNone(the_game.player1)
        self.assertIsNotNone(the_game.player2)

        self.assertIsInstance(the_game.player1.hand[0], card.Card)
        self.assertIsInstance(the_game.player2.hand[0], card.Card)

    def test_end(self):
        """Check ending conditions"""
        the_game = game.Game()
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

if __name__ == "__main__":
    unittest.main()
