from snakes import Snakes
from ladder import Ladder
from dice import Dice
from players import Player

class Board:
    def __init__(self):
        self.snake1 = Snakes()
        self.ladder1 = Ladder()
        self.dice1 = Dice()
        name, name2 = Player.get_player_name(self)
        self.player1 = Player(name)
        self.player2 = Player(name2)

