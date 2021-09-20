import constant
import game
import utils
import time
from snakes import Snakes
from ladder import Ladder

class Board:
    def check_win(self, player_name, player_pos):
        go = input(f'\t\t\t\t\t{player_name}: Please press "Enter" to roll the dice')
        dice_face = game.Game.dice_val()
        print(f"\t\t\t\t\tThe dice shows {dice_face}")
        player_pos = player_pos + dice_face
        player_pos = game.Game.get_snake_bite(player_name, player_pos)
        player_pos = Ladder.ladder_climb(player_name, player_pos)
        if player_pos == constant.HOME:
            utils.clear()
            print("\n\n\n\n\n\n\n\n\n")
            print(f"\t\t\t\t\t\t\tCongrats! {player_name} won!🎊🎉🎇")
            time.sleep(5)
            exit()
        elif player_pos < constant.HOME:
            print(f"\t\t\t\t\t{player_name}: Now.. You are {constant.HOME - player_pos} steps away from HOME!")
        elif player_pos > constant.HOME:
            player_pos = player_pos - dice_face
            print(f"\t\t\t\t\tOh oh! You just need {constant.HOME - player_pos} steps")
        return player_pos

    def final_player_pos(self, player_pos, player_name):
        player_pos = self.check_win(player_name, player_pos)
        input("\t\t\t\t\tPress 'Enter' to continue")
        print("\n\n\n\n")
        return player_pos

        