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

    def snakes_add(self, mouth, tail):
        self.snakes_dict[mouth] = tail

    def snakes_del(self):
        mouth = input("Enter the position of mouth that you want to delete? ")
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