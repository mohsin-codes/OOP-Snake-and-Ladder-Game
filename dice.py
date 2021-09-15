import constant
import random

class Dice:
    def __init__(self):
        dice_face = 0

    def dice_roll(self):
        dice_face = random.randint(1, constant.DICE_FACES)
        print("The dice shows", dice_face)

dice = Dice()
dice.dice_roll()