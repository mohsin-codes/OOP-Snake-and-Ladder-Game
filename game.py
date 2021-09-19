from board import Board
from snakes import Snakes
from ladder import Ladder
from dice import Dice
from players import Player

class Game:
    def __init__(self):
        self.snake1 = Snakes()
        self.ladder1 = Ladder()
        self.dice1 = Dice()
        name, name2 = Player.get_player_name(self)
        self.player1 = Player(name)
        self.player2 = Player(name2)
        self.board = Board()

    def start_game(self):
        while True:
            self.board.final_player_pos(self.player1.pos, self.player2.name)
            self.board.final_player_pos(self.player1.pos, self.player2.name)