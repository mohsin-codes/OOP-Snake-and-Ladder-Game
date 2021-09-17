from typing_extensions import TypeAlias
from ladder import Ladder

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
        for key, val in self.snakes_dict.items():
            print(f"{key} : {val}")

    def snakes_add(self):
        mouth_old = input("Enter the mouth position for snake that you want to delete : ")
        self.snakes_del(mouth_old)
        temp = True
        mouth_new = ""
        tail_new = ""
        while temp:
            mouth_new_in = input("Enter the new position for snake mouth : ")
            tail_new_in = input("Enter the new position for snake tail : ")
            for key, val in self.snakes_dict.items():
                print(key, val)
                if (mouth_new_in == key or mouth_new_in == val) or (tail_new_in == key or tail_new_in == val):
                    print("Values cannot be same as other snake mouth or tail. Please try different values.")
                    break
            for key, val in Ladder.ladders_dict.items():
                print(key, val)
                if (mouth_new_in == key or mouth_new_in == val) or (tail_new_in == key or tail_new_in == val):
                    print("Values cannot be same as other laddder values. Please try different values.")
            mouth_new = mouth_new_in
            tail_new = tail_new_in
            temp = False
        
        self.snakes_dict[str(mouth_new)] = tail_new


    def snakes_del(self, mouth):
        self.snakes_dict.pop(mouth)

# snake1 = Snakes()
# Snakes.snakes_list(snake1)
# mouth = input("Enter snake mouth position : ")
# tail = input("Enter snake tail position : ")
# Snakes.snakes_add(snake1, mouth, tail)
# Snakes.snakes_list(snake1)

# Snakes.snakes_del(snake1)
# Snakes.snakes_list(snake1)
# snake1.snakes_list()