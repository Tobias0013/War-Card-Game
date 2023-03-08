#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=== Welcome to the card War! ===

You will face an AI (or another player) in a battle
of who can win the others cards first. The players will play a card and 
the one with the highest card value, wins the cards

The game will end when one of the players has an empty hand.

--- Skriv spelregler ---

Type in 'start' to begin a game. Good luck!

"""
import sys

from war import shell

if __name__ == "__main__":
    """Displays doc string above and starts the shell loop."""
    print(__doc__)
    shell.Shell().cmdloop()
