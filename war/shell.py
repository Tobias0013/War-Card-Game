"""
This is our Shell class. Used to looping the game along with game logic.

Start by implementing modules needed.

    class Shell(cmd.Cmd)

The class has two class variables.
intro - Is printed when the shell starts
prompt - Is the prompt used for inputs

        intro = "Type help or ? to list commands."
        prompt = ">> "

User inputs 1 to play against computer, then enters his/her name.
If against another player, then enter his/her name and a name for opponent.
Then start the game.

        def do_start(self, _):

If it is player1's turn. Then play one of ther card to stack.
If player2 is not a player then run do_play again automaticly.
Else player2's turn. Then play one of ther card to stack.

Then run self.game.compare_cards()

If self.game.end() is true then change prompt to ">> "

        def do_start(self, _):

"""
import cmd
from time import sleep
from war import game


class Shell(cmd.Cmd):
    """Shell class to handle input, output and some game logic."""

    intro = "Type help or ? to list commands.\n"
    prompt = ">> "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start a game."""
        choice = input(
            "Please input the number of the desired mode"
            "\n1) Versus Computer\n2) Versus Player\n>> "
        )

        while True:
            if choice.isdigit():
                choice = int(choice)
                if choice in (1, 2):
                    break
            choice = input("Please input either 1 or 2 from the menu: ")

        is_player = False
        if choice == 2:
            is_player = True

        name1 = input("Player 1, what is your name?\n>> ")
        if choice == 2:
            name2 = input("Player 2, what is your name?\n>> ")
        else:
            name2 = "Computer"
        self.game.start(name1, name2, is_player)
        self.game.round_counter = 0
        self.prompt = f"({self.game.player1.name}) "

    def do_name_change(self, _):
        """Change current player name."""
        if self.prompt == ">> ":
            print("The game has not yet started.\nInput start to start game.")
            return

        if self.prompt == f"({self.game.player1.name}) ":
            self.game.player1.change_name()
            self.prompt = f"({self.game.player1.name}) "

        elif self.prompt == f"({self.game.player2.name}) ":
            self.game.player2.change_name()
            self.prompt = f"({self.game.player2.name}) "

    def do_play(self, _):
        """Player plays card from hand, \
            start war if both player played a card."""
        if self.prompt == ">> ":
            print("The game has not yet started.\nInput start to start game.")
            return

        if self.prompt == f"({self.game.player1.name}) ":
            self.game.player1.play_card()
            print(
                f"Card added to {self.game.player1.name}'s " +
                f"floor>> {self.game.player1.get_card()}"
            )
            self.prompt = f"({self.game.player2.name}) "

            if not self.game.player2.is_player:
                sleep(1)
                self.do_play("")
                return
        else:
            self.game.player2.play_card()
            print(
                f"Card added to {self.game.player2.name}'s " +
                f"floor>> {self.game.player2.get_card()}"
            )
            self.prompt = f"({self.game.player1.name}) "

        self.game.compare_cards()

        if self.game.end():
            self.prompt = ">> "

    def do_restart(self, _):
        """Restart game."""
        print("Restarting game....\n\n")
        self.game = game.Game()
        self.do_start("")

    def do_cheat(self, _):
        """Cheat, riggs war so that player 1 will win."""
        if self.prompt == ">> ":
            print("The game has not yet started.\nInput start to start game.")
            return
        
        self.game.cheat()

    def do_high_score(self, _):
        """Display high scores."""
        high_scores = self.game.high_scores

        if not high_scores:
            print("There is no high scores")
            return

        for i, score in enumerate(high_scores):
            print(f"{i + 1}. {score}")

    def do_exit(self, _):
        # pylint: disable=invalid-name
        """Leave the war."""
        print("Bye bye - see ya soon again")
        return True

    def do_quit(self, _):
        """Leave the war."""
        return self.do_exit(_)

    def do_q(self, _):
        """Leave the war."""
        return self.do_exit(_)

    def do_EOF(self, _):
        # pylint: disable=invalid-name
        """Leave the war."""
        return self.do_exit(_)

    def default(self, line):
        """Default unknown syntax message"""
        print(f"*** Unknown command: {line}\nType help or ? to list commands\n")
