#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from unittest import mock
from war import shell
from war import game
from war import card
from war import deck
from war import player


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = shell.Shell()
        exp = shell.Shell
        self.assertIsInstance(res, exp)

    @mock.patch("builtins.input", create=True)
    def test_start(self, mocked_input):
        """Test to start the war."""
        mocked_input.side_effect = ["1", "Roger"]

        shel = shell.Shell()
        shel.do_start("")

        self.assertIsInstance(shel.game.player1, player.Player)
        self.assertIsInstance(shel.game.player2, player.Player)
        self.assertFalse(shel.game.player2.is_player)

        mocked_input.side_effect = ["2", "Roger", "Malin"]
        shel.do_start("")
        self.assertTrue(shel.game.player2.is_player)

        self.assertEqual(shel.prompt, f"({shel.game.player1.name}) ")

    @mock.patch("builtins.input", create=True)
    def test_play(self, mocked_input):
        """Test play a card."""
        mocked_input.side_effect = ["2", "Roger", "Malin"]

        shel = shell.Shell()
        shel.do_start("")

        shel.do_play("")
        self.assertTrue(shel.game.player1.len_stack() == 1)
        res = shel.prompt == f"({shel.game.player2.name}) "
        self.assertTrue(res)
        shel.game.player1.clear_stack()

        shel.do_play("")
        self.assertTrue(shel.game.player2.len_stack() == 1)
        res = shel.prompt == f"({shel.game.player1.name}) "
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
