#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=== Welcome to the card War! ===

You will face an AI (or another player) in a battle
of who can win the others cards first. The players will play a card and 
the one with the highest card value, wins the cards

--- Rules ---
The deck is divided evenly among the players. Players play one card each
round and puts it on the floor and the one with the highest card value wins 
both cards and takes them to their hand. If both players card have the 
same value then a war begins. Both players play 2 more cards,
one face down and one face up. If the face-up cards are again equal then 
the battle repeats with another set of face-down/up cards. 
This repeats until one players face-up card is higher than their opponent's.

The game will end when one of the players has an empty hand.

Type in 'start' to begin a game. Good luck!

"""
import sys

from war import shell

if __name__ == "__main__":
    """Displays doc string above and starts the shell loop."""
    print(__doc__)
    shell.Shell().cmdloop()
