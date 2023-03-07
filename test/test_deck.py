#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from war import deck
from war import card



class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = deck.Deck()
        exp = deck.Deck
        self.assertIsInstance(res, exp)

    def test_generate_cards(self):
        """Test if length of cards is correct."""
        a_deck = deck.Deck()
        a_deck.cards.clear()
        a_deck._generate_cards()

        res = len(a_deck.cards) == 52
        self.assertTrue(res)
        self.assertTrue(isinstance(a_deck.cards[0], card.Card))

    def test_give_hands(self):
        """Test if give hand gives equal hands."""
        a_deck = deck.Deck()

        hand = ([], [])
        a_deck.give_hands(hand[0], hand[1])
        res = len(hand[0]) == 26 and len(hand[1]) == 26
        self.assertTrue(res)
        self.assertTrue(isinstance(hand[1][0], card.Card))
        self.assertTrue(isinstance(hand[0][0], card.Card))


if __name__ == "__main__":
    unittest.main()
