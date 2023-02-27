#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import game.Card


class TestGameClass(unittest.TestCase):  # noqa: H601
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = game.Card(0, 0)
        exp = game.Card
        self.assertIsInstance(res, exp)


if __name__ == "__main__":
    unittest.main()
