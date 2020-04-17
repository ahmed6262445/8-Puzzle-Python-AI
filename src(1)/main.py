import puzzle as game
import platform
from board import Board
from os import system
from time import sleep
import A_star_search as AI
from time import time
#import getch
os_name = platform.system().lower()
def clear():
    """
    Clears the console
    """
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


if __name__ == "__main__": # while True:
    input_loop_breaker = False
    while not input_loop_breaker:
        clear()
        user_board = input()
        user_board = list(user_board) # Converting str -> str list
        
        if len(user_board) != 9:
            print("Input Error!\nExiting...\nGoing Again...")
            sleep(1)
            continue
        else:
            for i in range(len(user_board)):
                try:
                    user_board[i] = int(user_board[i])
                    input_loop_breaker = True
                except ValueError:
                    print(ValueError)
                    print("Going Again...")
                    sleep(1)
                    input_loop_breaker = False
                    break
        is_solvable = game.is_solvable(user_board)
        if not is_solvable:
            print("Cannot be solved bye...")
            exit()
            sleep(2)
    # List input While Loop Ends
    if True:
        clear()

        steps = 0
        board = Board(3,3, user_board)
        win_state = game.win_game(board)

        while not win_state:
            clear()
            user_input = 0
            print(board.print_board())
            
            if False: # True if user wants to play
                print(f"Movement\n'w' to move UP\n's' to move DOWN\n'a' to move LEFT\n'd' to move Right\n\n")
                while True: 
                    user_input = getch.getch()
                    if user_input != 'w' and user_input != 's' and user_input != 'a' and user_input != 'd':
                        print("Invlaide Input...")
                        continue
                    move = None
                    if user_input == 'w':
                        move =  game.move(game.Direction.Up, board.board)
                    elif user_input == 's':
                        move = game.move(game.Direction.Down, board.board)
                    elif user_input == 'a':
                        move = game.move(game.Direction.Left, board.board)
                    elif user_input == 'd':
                        move = game.move(game.Direction.Right, board.board)
                    
                    if move != None:
                        board.board = move
                    win_state = game.win_game(board.board)
                    break 
            else:
                start = time()
                clear()
                print("Calculating...")
                win_state = AI.a_star(board.board)
                end = time()
                print(f"{end-start}")

            if win_state:
                print("You won!")
                # clear()
                # print("winning")
                # print(board.print_board())
        # Choice '1' While Loop Ends 
