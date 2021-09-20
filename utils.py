import os
from snakes import Snakes
from ladder import Ladder
import time


clear = lambda: os.system('cls')
#TODO : Fix the main_menu() part
def continue_game():
    user_choice = input('''
        Press 0 to go back to main menu
        Type 'Exit' to exit the game.
        ''')
    if user_choice == '0':
        pass
        # main.main_func.main_menu()
    elif user_choice.lower() == 'exit':
        exit()


def settings():
    clear()
    while True:
        setting_input = input(f''' 
        Press 1 - Change Snakes Position
        Press 2 - Change Ladder Position
        Press 3 - Go Back
        Enter your choice - \
        ''')
        if setting_input == "1":
            snake1 = Snakes()
            snake1.snakes_list()
            snake1.snakes_add()
            # snake1.snakes_list()
        elif setting_input == "2":
            pass
            # change_ladder_pos()
        elif setting_input == "3":
            pass
            # continue_game()
        else:
            input("\n\tWrong input. Please Try Again!")
            clear()
            continue


def rules():
    clear()
    print('''
    1. When a piece comes on a number which lies on the top of a snake (face of the snake), 
        then the piece/token will land below to the bottom of the snake (tail of it) that can also be said as an unlucky move.

    2. If somehow the piece falls on the ladder base, 
        it will immediately climb to the top of the ladder (which is considered to be a lucky move).
    
    3. Whereas if a player lands on the bottom of the snake or top of a ladder, 
        the player will remain in the same spot (same number) and will not get affected by any particular rule. 
        The players can never move down ladders.
    
    4. The pieces of different players can overlap each other without knocking out anyone. 
        There is no concept of knocking out by opponent players in Snakes and Ladders.
    
    5. To win, the player needs to roll the exact number of die to land on the number 100. 
        If he/she fails to do so, then the player needs to roll the die again in the next turn. 
        For example, if a player is on the number 98 and the die roll shows the number 4, 
        then the player cannot move its piece until he/she gets a 2 to win or 1 to be on the 99th number.
    ''')
    continue_game()

def how_to_play():
    clear()
    print('''
    1. Each player puts their name and tha game starts.
    
    2. Take it in turns to roll the dice. Counter automatically moves forward the number of spaces shown on the dice.
    
    3. If your counter lands at the bottom of a ladder, you can move up to the top of the ladder.
    
    4. If your counter lands on the head of a snake, you must slide down to the bottom of the snake.
    
    5. The first player to get to the space that says 'home' is the winner.
    ''')
    continue_game()

def dots():
    dices = "🎲🎲🎲🎲🎲"
    for i in range(len(dices)):
        print(dices[i],sep="", end="", flush=True)
        time.sleep(0.3)
    print()