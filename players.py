import utils
from os import name


class Player:
    def __init__(self, name):
        self.name = name
        self.pos = 0

    def get_player_name(self):
        utils.clear()
        name = input("Enter Player 1 Name : ")
        name2 = input("Enter Player 2 Name : ")
        return name, name2
