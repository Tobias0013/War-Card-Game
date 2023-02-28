"""
Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import Card
import Game
import Player


class Shell(cmd.Cmd):
    """Shell class to handle input and game logic"""

    intro = "Welcome to the game. Type help or ? to list commands.\n"
    prompt = ">> "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = Game.Game()

    def do_start(self, _):
        """Start the game."""

        choice = input('=== Welcome to the card game War! === \nPlease input the number of the desired mode'
        '\n1) Versus Computer\n2) Versus Player\n>> ')

        while True:
            if choice.isdigit():
                choice = int(choice)
                if choice == 1 or choice == 2:
                    break
            choice = input('Please input either 1 or 2 from the menu')

        is_player = False
        if choice == 2:
            is_player = True

        name1 = input('Player 1, what is your name?\n>> ')
        if choice == 2:
            name2 = input('Player 2, what is your name?\n>> ')
        else:
            name2 = "Computer"
        self.game.start(name1, name2, is_player)
        self.prompt = f"({self.game.player1.name}) "


    def do_name_change(self):
        Player.Player().change_name()

    def do_play(self, _):
        """"Player plays card from hand"""
        if self.prompt == f"({self.game.player1.name}) ":
            #tar ett kort från handen och lägger på bordet (player1)
            self.game.player1.play_card()
            print(f"Card added to player1 stack>> {self.game.player1.stack[-1].get_value()}")
            self.prompt = f"({self.game.player2.name}) "
        else:
            #tar ett kort från handen och lägger på bordet (player2)
            self.game.player2.play_card()
            print(f"Card added to player2 stack>> {self.game.player2.stack[-1].get_value()}")
            self.prompt = f"({self.game.player1.name}) "

        self._check_cards()
        self.game.round_counter += 1

        if self.game.end():
            self.prompt = ">> "


    def _check_cards(self):
        #if both stacks have card in them check witch is bigger than give both card to that player
        if len(self.game.player1.stack) > 0 and len(self.game.player2.stack) > 0:

            #This checks if player1 card has higher value
            if self.game.player1.stack[-1].get_value() > self.game.player2.stack[-1].get_value():
                print(f"Player1 has higher card")
                print(f"Player1 card: {self.game.player1.stack[-1].get_value()}")
                print(f"Player2 card: {self.game.player2.stack[-1].get_value()}")
                self.game.player1.add_stack(self.game.player1.get_stack())#give player1 stack to player1 hand
                self.game.player1.add_stack(self.game.player2.get_stack())#give player2 stack to player1 hand
                print(f"Player1 hand len: {len(self.game.player1.hand)} Player2 hand len: {len(self.game.player2.hand)}")

            #This checks if player2 card has higher value    
            elif self.game.player2.stack[-1].get_value() > self.game.player1.stack[-1].get_value():
                print(f"Player2 has higher card")
                print(f"Player1 card: {self.game.player1.stack[-1].get_value()}")
                print(f"Player2 card: {self.game.player2.stack[-1].get_value()}")
                self.game.player2.add_stack(self.game.player1.get_stack())#give player1 stack to player2 hand
                self.game.player2.add_stack(self.game.player2.get_stack())#give player2 stack to player2 hand
                print(f"Player1 hand len: {len(self.game.player1.hand)} Player2 hand len: {len(self.game.player2.hand)}")

            #this hapends if both players card have same value
            elif self.game.player1.stack[-1].get_value() == self.game.player2.stack[-1].get_value():
                #plays 2 cards from each hand
                self.game.player1.play_card()
                self.game.player1.play_card()
                self.game.player2.play_card()
                self.game.player2.play_card()
                print("both player have same value")
                print(f"Player1 card: {self.game.player1.stack[-1].get_value()}")
                print(f"Player2 card: {self.game.player2.stack[-1].get_value()}")
                print(f"Player1 hand len: {len(self.game.player1.hand)} Player2 hand len: {len(self.game.player2.hand)}")
                self._check_cards()

    def do_cheat(self, _):
        """Cheat."""
        # rigga en vinst åt spelare 1
        # cleara stack och hand för båda spelare
        self.game.player1.stack.clear()
        self.game.player1.hand.clear()
        self.game.player2.stack.clear()
        self.game.player2.hand.clear()
        # lägg till ett högt kort til spelare 1 hand
        # lägg till lågt kort till spelare 2 hand
        self.game.player1.hand.append(Card.Card(11, 0))
        self.game.player2.hand.append(Card.Card(0, 0))


    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye - see ya soon again")
        return True

    def do_quit(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
