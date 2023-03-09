#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=== Welcome to the card War! ===

You will face an AI (or another player) in a battle
of who can win the others cards first. The players will play a card and 
the one with the highest card value, wins the cards

The game will end when one of the players has an empty hand.

The deck is divided evenly among the players. Player plays one card each round to a stack
and the one with highest card value wins both cards and takes them to their hand.
If both players card have the same value then a war begins. Then both players play 2 more cards,
one unknown and one known. when 

This repeats until one player has won all cards from the other player.


Type in 'start' to begin a game. Good luck!

"""
import sys

from war import shell

if __name__ == "__main__":
    """Displays doc string above and starts the shell loop."""
    print(__doc__)
    shell.Shell().cmdloop()
