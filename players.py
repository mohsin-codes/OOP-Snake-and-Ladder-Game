import utils
from os import name


class Player:
    def __init__(self, name):
        self.name = name
        self.pos = 0

    def get_player_name(self):
        utils.clear()
        name = input("\t\t\t\t\tEnter Player 1 Name : ")
        name2 = input("\t\t\t\t\tEnter Player 2 Name : ")
        return name, name2
