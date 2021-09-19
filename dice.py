import constant
import random
import utils


class Dice:
    def __init__(self):
        dice_face = 0

    def get_dice_face(player_name):
        go = input(f'\t\t\t\t\t{player_name}: Please press "Enter" to roll the dice')
        print("\t\t\t\t\tRolling the dice", end="")
        utils.dots()
        dice_face = random.randint(1,constant.DICE_FACES)
        print(f"\t\t\t\t\tThe dice shows {dice_face}")
        return dice_face
