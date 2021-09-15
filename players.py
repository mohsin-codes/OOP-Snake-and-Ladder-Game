class Player:
    def __init__(self, name):
        self.name = name
        self.pos = 0
        
    def player_name(self):
        print(self.name)

    def player_pos(self):
        print(self.pos)

    def player_complete_info(self):
        print("Name :  ", self.name)
        print("Position : ", self.pos )

    def update_player_pos(self, new_pos):
        self.pos = new_pos



# name = input("Please give a valid name for player : ")
# player1 = Player(name)

# player1.player_name()
# player1.player_pos()
# player1.player_complete_info()
# player1.update_player_pos(25)
# player1.player_pos()