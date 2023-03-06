"""
Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
from war import game


class Shell(cmd.Cmd):
    """Shell class to handle input and war logic"""

    intro = "Welcome to the war. Type help or ? to list commands.\n"
    prompt = ">> "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start the war."""

        choice = input('=== Welcome to the card war War! === \nPlease input the number of the desired mode'
                       '\n1) Versus Computer\n2) Versus Player\n>> ')

        while True:
            if choice.isdigit():
                choice = int(choice)
                if choice in (1, 2):
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
        """Change player name."""
        pass

    def do_play(self, _):
        """"Player plays card from hand"""
        if self.prompt == f"({self.game.player1.name}) ":
            # tar ett kort från handen och lägger på bordet (player1)
            self.game.player1.play_card()
            print(f"Card added to player1 stack>> {self.game.player1.get_card()}")
            self.prompt = f"({self.game.player2.name}) "
        else:
            # tar ett kort från handen och lägger på bordet (player2)
            self.game.player2.play_card()
            print(f"Card added to player2 stack>> {self.game.player2.get_card()}")
            self.prompt = f"({self.game.player1.name}) "

        self.game.compare_cards()

        if self.game.end():
            self.prompt = ">> "

    def do_cheat(self, _):
        """Cheat, riggs war so that player 1 will win."""
        self.game.cheat()

    def do_high_score(self, _):
        """Display high scores."""
        high_scores = self.game.high_scores

        for i, score in enumerate(high_scores):
            print(f"{i + 1}. {score}")

    def do_exit(self, _):
        """Leave the war."""
        print("Bye bye - see ya soon again")
        return True

    def do_quit(self, arg):
        """Leave the war."""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Leave the war."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        """Leave the war."""
        return self.do_exit(arg)
