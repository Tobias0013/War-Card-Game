from Player import Player


class High_score:
    def __init__(self, rounds, player_winner, player_looser):
        self.rounds = rounds
        self.player_winner = player_winner
        self.player_looser = player_looser

    def __str__(self):
        return f"Rounds played: {self.rounds} //Winner: {self.player_winner.name} //Loser: {self.player_looser.name}"
