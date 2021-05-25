"""A Game Class that uses the Leaderboard Singleton"""

from leaderboard import Leaderboard
from interface_game import IGame


class Game2(IGame):
    """Game2 implements IGame"""

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)
