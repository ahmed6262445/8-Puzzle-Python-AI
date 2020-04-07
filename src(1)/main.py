import puzzle as game
import platform
from board import Board
from os import system
from time import sleep
os_name = platform.system().lower()
def clear():
    """
    Clears the console
    """
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

import getch



def invserion_count():
    # arr = [0,2,3,4,1,6,5,8,7]
    arr = [5,2,4,3,8,7,6,0,1]
    inv_count = 0

    for i in range(8):
        for j in range(i+1, 8):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


# print(invserion_count())
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
            if True:#steps == 0:
                print(f"Movement\n'w' to move UP\n's' to move DOWN\n'a' to move LEFT\n'd' to move Right\n\n")
                
                while True:
                    # user_input = input("Enter initial input: ")
                    user_input = getch.getch()

                    if user_input != 'w' and user_input != 's' and user_input != 'a' and user_input != 'd':
                        print("Invlaide Input...")
                        continue
                    break 
            else:
                # Ai moves
                pass

            if user_input == 'w':
                game.move(game.Direction.Up, board)
            elif user_input == 's':
                game.move(game.Direction.Down, board)
            elif user_input == 'a':
                game.move(game.Direction.Left, board)
            elif user_input == 'd':
                game.move(game.Direction.Right, board)

            win_state = game.win_game(board)

            if win_state:
                clear()
                print(board.print_board())
        # Choice '1' While Loop Ends 