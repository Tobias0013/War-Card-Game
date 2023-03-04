#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from war import card


class Test_card(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = card.Card(2, 0)
        exp = card.Card
        self.assertIsInstance(res, exp)

    def test_get_value(self):
        """Test if get_value() returns right value"""
        a_card = card.Card(2, 0)

        res = a_card.get_value()
        exp = 2
        self.assertEqual(res, exp)

        a_card = card.Card(14, 0)

        res = a_card.get_value()
        exp = 14
        self.assertEqual(res, exp)

    def test_str(self):
        """Test str method."""
        a_card = card.Card(2, 0)

        res = a_card.__str__()
        exp = "number=2,suite=Sute.HEARTS,color=Color.RED"
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
