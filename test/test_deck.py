#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import game.Deck


class TestGameClass(unittest.TestCase):  # noqa: H601
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = game.Deck()
        exp = game.Deck
        self.assertIsInstance(res, exp)

    def test_generate_cards(self):
        """Test generate cards."""
        deck = game.Deck()
        deck._generate_cards()

        res = len(deck.cards) == 52
        self.assertTrue(res)

    def test_give_hands(self):
        """Test if give hand gives equal hands."""
        deck = game.Deck()

        hand = ([], [])
        deck.give_hands(hand[0], hand[1])
        res = len(hand[0]) == 26
        self.assertTrue(res)
        res = len(hand[1]) == 26
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
