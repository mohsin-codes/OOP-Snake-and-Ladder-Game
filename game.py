from board import Board
from snakes import Snakes
from ladder import Ladder
from dice import Dice
from players import Player
import utils

class Game:
    def __init__(self):
        self.snake1 = Snakes()
        self.ladder1 = Ladder()
        name, name2 = Player.get_player_name(self)
        self.player1 = Player(name)
        self.player2 = Player(name2)
        self.board = Board()

    def dice_val():
        return Dice.get_dice_face()

    def start_game(self):
        while True:
            utils.clear()
            self.player1.pos = self.board.final_player_pos(self.player1.pos, self.player1.name)
            self.player2.pos = self.board.final_player_pos(self.player2.pos, self.player2.name)


