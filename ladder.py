import utils
import time
import snakes

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
        while True:
            bottom_old = input("\n\t\t\t\t\tEnter the bottom position for ladder that you want to delete : ")
            try:
                self.ladder_del(bottom_old)
                break
            except KeyError as ke:
                print("\t\t\t\t\tKey not found. Try again")
            except:
                print("Another exception found")
                raise
        bottom_new = ""
        top_new = ""
        while True:
            temp = False
            bottom_new_in = input("\t\t\t\t\tEnter the new position for Ladder Bottom : ")
            top_new_in = input("\t\t\t\t\tEnter the new position for Ladder Top : ")
            for key, val in self.ladders_dict.items():
                # print(key, val)
                if (bottom_new_in == key or bottom_new_in == val) or (top_new_in == key or top_new_in == val):
                    print("\t\t\t\t\tValues cannot be same as other ladder bottom or top. Please try different values.")  
                    temp = True      
            for key, val in snakes.Snakes.snakes_dict.items():
                # print(key, val)
                if (bottom_new_in == key or bottom_new_in == val) or (top_new_in == key or top_new_in == val):
                    print("\t\t\t\t\tValues cannot be same as other snake values. Please try different values.")
                    temp = True
                else:
                    bottom_new = bottom_new_in
                    top_new = top_new_in
            if temp == True:
                continue
            else:
                utils.clear()
                print("\t\t\t\t\tChanged Successfully")
                time.sleep(2)
                break
        Ladder.ladders_dict[bottom_new] = top_new

    def ladder_del(self, bottom):
        self.ladders_dict.pop(bottom)

    def ladder_list(self):
        utils.clear()
        print("\t\t\t\t\tLadder Bottom\t\tLadder Top")
        for key, val in self.ladders_dict.items():
            print(f"\t\t\t\t\t{key}\t\t:\t{val}")

    @classmethod
    def ladder_climb(cls, player_name, player_pos):
        for key, val in cls.ladders_dict.items():
            if player_pos == int(key):
                print(f"\t\t\t\t\tGreat!!😁 {player_name} found a ladder😎. Move up to {val}")
                player_pos = int(val)
            else:
                continue
        return player_pos



