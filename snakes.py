from os import closerange
from ladder import Ladder
import utils
import time

class Snakes:
    snakes_dict = {
    "27" : "5",
    "40" : "3",
    "43" : "18", 
    "54" : "31",
    "66" : "45",
    "76" : "58",
    "89" : "53",
    "99" : "41"
    }

    def snakes_list(self):
        utils.clear()
        print("\t\t\t\t\tSnake Mouth\t\tSnake Tail")
        for key, val in self.snakes_dict.items():
            print(f"\t\t\t\t\t{key}\t\t:\t{val}")

    def snakes_add(self):
        while True:
            mouth_old = input("\n\t\t\t\t\tEnter the mouth position for snake that you want to delete : ")
            try:
                self.snakes_del(mouth_old)
                break
            except KeyError as ke:
                print("\t\t\t\t\tKey not found. Try again")
            except:
                print("Another exception found")
                raise
        mouth_new = ""
        tail_new = ""
        while True:
            temp = False
            mouth_new_in = input("\t\t\t\t\tEnter the new position for snake mouth : ")
            tail_new_in = input("\t\t\t\t\tEnter the new position for snake tail : ")
            for key, val in self.snakes_dict.items():
                # print(key, val)
                if (mouth_new_in == key or mouth_new_in == val) or (tail_new_in == key or tail_new_in == val):
                    print("\t\t\t\t\tValues cannot be same as other snake mouth or tail. Please try different values.")  
                    temp = True      
            for key, val in Ladder.ladders_dict.items():
                # print(key, val)
                if (mouth_new_in == key or mouth_new_in == val) or (tail_new_in == key or tail_new_in == val):
                    print("\t\t\t\t\tValues cannot be same as other ladder values. Please try different values.")
                    temp = True
                else:
                    mouth_new = mouth_new_in
                    tail_new = tail_new_in
            if temp == True:
                continue
            else:
                utils.clear()
                print("\t\t\t\t\tChanged Successfully")
                time.sleep(2)
                break
        Snakes.snakes_dict[mouth_new] = tail_new
        
    @classmethod
    def snake_bite(cls, player_name, player_pos):
        for key, val in cls.snakes_dict.items():
            if player_pos == int(key):
                print(f"\t\t\t\t\tOh no!😯 {player_name} got bitten by a snake🐍😔. Go back to {val}")
                player_pos = int(val)
            else:
                continue
        return player_pos

    def snakes_del(self, mouth):
        self.snakes_dict.pop(mouth)
