import game
import constant


class Board:



    def check_win(self, player_name, player_pos):
        dice_face = game.dice1.get_dice_face(player_name)
        player_pos = player_pos + dice_face
        player_pos = game.snake1.snake_bite(player_name, player_pos)
        player_pos = game.ladder1.ladder_climb(player_name, player_pos)
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