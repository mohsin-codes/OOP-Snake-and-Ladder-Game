import constant
import game
from dice import Dice

class Board:
    def check_win(self, player_name, player_pos):
        go = input(f'\t\t\t\t\t{player_name}: Please press "Enter" to roll the dice')
        dice_face = game.Game.dice_val()
        print(f"\t\t\t\t\tThe dice shows {dice_face}")
        player_pos = player_pos + dice_face
        # player_pos = Game.snake1.snake_bite(player_name, player_pos)
        # player_pos = Game.ladder1.ladder_climb(player_name, player_pos)
        if player_pos == constant.HOME:
            print(f"\t\t\t\t\tCongrats! {player_name} won!🎊🎉🎇")
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
        return player_pos