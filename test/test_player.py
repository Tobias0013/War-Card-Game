#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from war import player

class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        exp = player.Player("a", [1, 2, 3, 4], False)
        self.assertIsInstance(exp, player.Player)
    
    def test_play_card(self):
        exp = player.Player("a", [1, 2, 3, 4], False)
        ref = [exp, exp, exp, exp]

        ref[0].play_card()
        ref[0].play_card()
        self.assertEqual(len(ref), len(ref))

    def test_clearing_hand_stack(self):
        exp = player.Player("Eddie", [1,2,3], ['a', 'b', 'c'])
        ref = [exp, exp, exp, exp]

        ref[0].clear_hand()
        ref[0].clear_stack()

        self.assertEqual(ref[0].hand_empty(), ref[0].stack_empty())
