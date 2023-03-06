
"""High score class."""


class High_score:
    """High score class."""
    def __init__(self, rounds, player_winner, player_looser):
        """High score constructor."""
        self.rounds = rounds
        self.player_winner = player_winner
        self.player_looser = player_looser

    def __str__(self):
        """High score to string."""
        return f"Rounds played: {self.rounds} //Winner: {self.player_winner.name} //Loser: {self.player_looser.name}"
