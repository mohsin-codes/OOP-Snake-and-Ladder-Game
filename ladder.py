class Ladder:
    ladders_dict = {
    "4" : "25",
    "13" : "46",
    "33" : "49",
    "42" : "63",
    "50" : "69",
    "62" : "81",
    "74" : "92"
    }

    def ladder_add(self):
        bottom = input("Enter the bottom position of ladder : ")
        top = input("Enter top position of ladder : ")
        self.ladders_dict[bottom] = top

    def ladder_del(self):
        bottom = input("Enter the bottom of ladder that you want to delete : ")
        self.ladders_dict.pop(bottom)

    def ladder_list(self):
        for key, val in self.ladders_dict.items():
            print(f"{key} : {val}")

# ladder1 = Ladder()
# Ladder.ladder_list(ladder1)
# Ladder.ladder_add(ladder1)
# Ladder.ladder_list(ladder1)
# Ladder.ladder_del(ladder1)
# Ladder.ladder_list(ladder1)

