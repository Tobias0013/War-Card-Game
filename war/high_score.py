"""High_score file."""


class High_score:
    """High score class."""

    def __init__(self, rounds, player_winner, player_looser):
        """High score constructor."""
        self.rounds = rounds
        self.player_winner = player_winner
        self.player_looser = player_looser

    def __str__(self):
        """Return high score as string."""
        return f"Rounds played: {self.rounds} //\
            Winner: {self.player_winner.name} //\
                Loser: {self.player_looser.name}"

    def __eq__(self, other):
        """Compare if two high scores are equal."""
        if isinstance(other, High_score):
            return (
                self.rounds == other.rounds
                and self.player_winner.name == other.player_winner.name
                and self.player_looser.name == other.player_looser.name
            )
        return False
