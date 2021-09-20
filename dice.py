import constant
import random
import utils


class Dice:
    
    dice_face = 0

    def __init__(self):
        pass

    def get_dice_face():
        print("\t\t\t\t\tRolling the dice", end="")
        utils.dots()
        dice_face = random.randint(1,constant.DICE_FACES)
        return dice_face

