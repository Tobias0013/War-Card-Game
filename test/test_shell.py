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
        mocked_input.side_effect = ["1", "test"]

        shel = shell.Shell()
        shel.do_start()
        self.assertIsInstance(shel.game, game.Game)
        self.assertIsInstance(shel.game.player1, player.Player)
        self.assertIsInstance(shel.game.player2, player.Player)

    def test_prompt(self):
        """Test prompt changes correct."""
        shel = shell.Shell()
        res = shel.prompt
        exp = ">> "
        self.assertEqual(res, exp)

        shel.do_start()
        res = shel.prompt
        exp = ">> "
        self.assertEqual(res, exp)

        shel.do_play()

    def test_play(self):
        """Test when player1 and player2 plays there turns."""
        shel = shell.Shell()
        shel.do_start()
        shel.do_play()

        res = shel.game.player1.get_card() is not None
        self.assertTrue(res)
        shel.do_play()

        res = shel.game.player2.get_card() is not None
        self.assertTrue(res)

    def test_cheat(self):
        self.shell.do_start()
        self.shell.do_cheat()
        self.assertEqual(self.shell.Game.winner, self.shell.Game.player1)


if __name__ == "__main__":
    unittest.main()
