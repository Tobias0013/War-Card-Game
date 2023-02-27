"""
Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import game


class Shell(cmd.Cmd):
    """Shell class to handle input and game logic"""

    intro = "Welcome to the game. Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start the game with a new number."""
        msg = (
            "I am ready and is now thinking of a new secret number"
            " between {} and {}."
        )
        self.game.start()
        print(msg.format(self.game.low(), self.game.high()))

    def do_cheat(self, _):
        """Cheat to view the secret number."""
        number = self.game.cheat()
        print(f"Cheater... the number is {number}.")

    def do_guess(self, arg):
        """Do a guess of a number."""
        msg = "Missing argument on the number you are guessing. Try 'guess 42'."
        if not arg:
            print(msg)
            return

        if self.game.times_guessed >= 5:
            print("you have already tried 5 times")
            return

        a_number = int(arg)
        try:
            guess = self.game.guess(a_number)
            print(f"You're guess is -> {guess}")
        except ValueError as error:
            print(error)

        if guess == "Correct":
            print(self.game.end_of_game("won"))

        if self.game.times_guessed >= 5:
            print(self.game.end_of_game("lose"))

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
