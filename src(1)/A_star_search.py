import puzzle as game
from copy import deepcopy
from direction import Direction,Coordinate
from board import Board
from time import sleep

# def search_move(start_state, g):
#     lowest_h = float('inf')
#     # return_node = None
#     return_move = None
#     x = 0
#     y = 0
#     if game.is_solvable(start_state.board):
#         # last_state = deepcopy(start_state)
#         for i in range(4):
#             node = deepcopy(start_state)
#             x,y = game.find_empty_space(node)
#             if i == 0:
#                 move = Direction.Up
#                 inc_x,inc_y = Coordinate.Up.value
#             elif i == 1:
#                 move = Direction.Down
#                 inc_x,inc_y = Coordinate.Down.value
#             elif i == 2:
#                 move = Direction.Left
#                 inc_x,inc_y = Coordinate.Left.value
#             elif i == 3:
#                 move = Direction.Right
#                 inc_x,inc_y = Coordinate.Right.value
#             x = inc_x + x
#             y = inc_y + y
#             if game.is_valid_move(x,y, len(start_state.board)):
#                 # print(node.board)
#                 game.move(move, node)
#                 # h = find_hammingdistance(node)
#                 # print(i)
#                 # print(node.board)
#                 # print(h)
#                 # print(g)
#                 # print("")
#                 # sleep(5)
#                 if h < lowest_h:
#                     lowest_h = h+g
#                     # last_state = deepcopy(node)
#                     return_move = move
#     return return_move


class Node:
    def __init__(self, state, g_value):
        self.state = state
        self.g_value = g_value
        self.f_value = self.calculate_f()

    def find_hammingdistance(self) -> int:
        """
            Finds the number of misplace tiles in the current state of the board with the winning state
        Parameters:
            current_state (Board obj) : The current state of the object (Board)
        Return:
            Returns the count of misplaced tiles
        """
        count = 0
        board_len = len(self.state.board)
        for i in range(board_len):
            for j in range(board_len):
                if self.state.board[i][j] and self.state.board[i][j] != game.win_state[i][j]:
                    count += 1
        return count

    def calculate_f(self):
        return self.find_hammingdistance() + self.g_value

from queue import Queue
def ai_move(current_state: Board):
    """
        Bot (Artifical Intelligence plays the game)
    Parameters:
        current_state (Board obj): Current State of the board
    Returns:
        Returns if win state is achieved or not
    """
    # queue = Queue()
    closed_list = []
    open_list = []
    return_list = []

    parent_node = Node(deepcopy(current_state), 0)
    open_list.append(deepcopy(parent_node))
    while len(open_list) != 0:
        parent_node = deepcopy(open_list[0])
        return_list.append(deepcopy(parent_node.state))

        if parent_node.find_hammingdistance() == 0: # terminating condition
            print("hello")
            return_tuple = (return_list, parent_node.g_value,game.win_game(parent_node.state))
            return return_tuple

        # Generating child nodes
        for i in range(4):
            temp_node = deepcopy(parent_node)

            x,y = game.find_empty_space(temp_node.state)
            if i == 0:
                move = Direction.Up
                inc_x,inc_y = Coordinate.Up.value
            elif i == 1:
                move = Direction.Down
                inc_x,inc_y = Coordinate.Down.value
            elif i == 2:
                move = Direction.Left
                inc_x,inc_y = Coordinate.Left.value
            elif i == 3:
                move = Direction.Right
                inc_x,inc_y = Coordinate.Right.value
            x = inc_x + x
            y = inc_y + y

            print(temp_node.state)
            if game.is_valid_move(x,y, len(temp_node.state.board)):
                game.move(move, temp_node.state)
                print(temp_node.state)
                sleep(5)
                if temp_node not in open_list:
                    child_node = Node(deepcopy(temp_node.state), temp_node.g_value+1)
                    open_list.append(deepcopy(child_node))
            closed_list.append(parent_node)
            del open_list[0]

    # g = 1
    # while current_state.board != game.win_state:
    #     move = search_move(current_state,g)
    #     g += 1
    #     game.move(move, current_state)
    # return True


# start = [
#     [6,0,7],
#     [8,4,5],
#     [2,1,3]
# ]
# obj = Board(3,3,[6,0,7,8,4,5,2,1,3])
# print(game.find_empty_space(obj))

# x,y = Coordinate.Left.value
# print(game.is_valid_move(0,-1,3))