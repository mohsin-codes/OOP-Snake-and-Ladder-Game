import utils



class main_func:

    def continue_game():
        user_choice = input('''
            Press 0 to go back to main menu
            Type 'Exit' to exit the game.
            ''')
        if user_choice == '0':
            pass
        elif user_choice.lower() == 'exit':
            exit()

    def main_menu_options(self, choice):
        if choice ==  1:
            utils.start_game()
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
        utils.clear()
        user_choice=0
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
            self.main_menu()

game = main_func()
game.main_menu()