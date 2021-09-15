import snakes, ladder, dice, players

class Board:
    def __init__(self):
        self.snake1 = snakes.Snakes()
        self.ladder1 = ladder.Ladder()
        self.dice1 = dice.Dice()
        self.player1 = players.Player()
        self.player2 = players.Player()

    
