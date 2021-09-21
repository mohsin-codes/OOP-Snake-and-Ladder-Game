from os import name
import utils
from game import Game
import time
import animation

class main_func:

    def main_menu_options(self, choice):
        if choice ==  1:
            game = Game()
            game.start_game()
        elif choice == 2:
            utils.rules()
        elif choice == 3:
            utils.how_to_play()
        elif choice == 4:
            utils.settings()
        elif choice == 5:
            utils.clear()
            exit()


    def main_menu(self):
        user_choice=0
        while True:
            choice = input('''
                                                        Welcome to the Snakes🐍 and Ladder Game!
                                                            
                                                            Press 1 - Start the game ▶
                                                            Press 2 - Rules📕
                                                            Press 3 - How to Play ❓ 
                                                            Press 4 - Settings⚙
                                                            Press 5 - Exit🚪
                                                            Enter your choice - \
            ''')
            try:
                user_choice = int(choice)
            except ValueError as ve:
                print("\n\n")
                input("\t\t\t\t\t\tYou are trying to input wrong value. Try again by pressing 'Enter'")     
            if user_choice == 1 or 2 or 3 or 4 or 5: 
                self.main_menu_options(user_choice)
            else:
                input("Wrong Input! Try Again")
                



if __name__ == "__main__":
    print("\n\n\n\n\n\t\t\t\t\tPlease make the window full screen to enjoy the game.")
    time.sleep(3)
    choice = animation.main_func()
    if choice.lower() == 's':
        utils.clear()
        start = main_func()
        start.main_menu()
    elif choice.lower() == 'e':
        utils.clear()
        exit()
    else:
        print("Try Again!")
        utils.clear()