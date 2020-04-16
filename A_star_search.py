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


# class Node:
#     def __init__(self, state, parent=None):
#         self.state = state
#         self.parent = parent
#         self.g_value = 0

#         if self.parent != None:
#             self.g_value = parent.g_value+1
#         self.h_value = self.find_hammingdistance()
#         self.f_value = self.calculate_f()

#     def get_eculidian_cost(state):
#         cost = 0
#         board_len = len(state.board)
#         for i in range(board_len):
#             for j in range(board_len):
#                 pos = get_pos


#     def find_hammingdistance(self) -> int:
#         """
#             Finds the number of misplace tiles in the current state of the board with the winning state
#         Parameters:
#             current_state (Board obj) : The current state of the object (Board)
#         Return:
#             Returns the count of misplaced tiles
#         """
#         count = 0
#         board_len = len(self.state.board)
#         for i in range(board_len):
#             for j in range(board_len):
#                 if self.state.board[i][j] and self.state.board[i][j] != game.win_state[i][j]:
#                     count += 1
#         return count

#     def calculate_f(self):
#         return self.h_value + self.g_value
    
#     def get_neighbor(self,i):
#         child_state = deepcopy(self.state)
#         x,y = game.find_empty_space(child_state)
#         if i == 0:
#             move = Direction.Up
#             inc_x,inc_y = Coordinate.Up.value
#         elif i == 1:
#             move = Direction.Down
#             inc_x,inc_y = Coordinate.Down.value
#         elif i == 2:
#             move = Direction.Left
#             inc_x,inc_y = Coordinate.Left.value
#         elif i == 3:
#             move = Direction.Right
#             inc_x,inc_y = Coordinate.Right.value
#         x = inc_x + x
#         y = inc_y + y
#         if game.is_valid_move(x,y, len(child_state.board)):
#             game.move(move, child_state)
#             return Node(child_state, self)
#         return None


# # from queue import Queue
# # def ai_move(current_state: Board):
# #     """
# #         Bot (Artifical Intelligence plays the game)
# #     Parameters:
# #         current_state (Board obj): Current State of the board
# #     Returns:
# #         Returns if win state is achieved or not
# #     """
# #     # queue = Queue()
# #     closed_list = []
# #     open_list = []
# #     return_list = []

# #     parent_node = Node(deepcopy(current_state), 0)
# #     open_list.append(deepcopy(parent_node))
# #     while len(open_list) != 0:
# #         parent_node = deepcopy(open_list[0])

# #         if parent_node.find_hammingdistance() == 0: # terminating condition
# #             print("hello")
# #             return_tuple = (closed_list, parent_node.g_value,game.win_game(parent_node.state))
# #             return return_tuple

# #         # Generating child nodes
# #         for i in range(4):
            # temp_node = deepcopy(parent_node)

            # x,y = game.find_empty_space(temp_node.state)
            # if i == 0:
            #     move = Direction.Up
            #     inc_x,inc_y = Coordinate.Up.value
            # elif i == 1:
            #     move = Direction.Down
            #     inc_x,inc_y = Coordinate.Down.value
            # elif i == 2:
            #     move = Direction.Left
            #     inc_x,inc_y = Coordinate.Left.value
            # elif i == 3:
            #     move = Direction.Right
            #     inc_x,inc_y = Coordinate.Right.value
            # x = inc_x + x
            # y = inc_y + y

# #             # print(i)
# #             # print(temp_node.state.board)
#             # if game.is_valid_move(x,y, len(temp_node.state.board)):
#             #     game.move(move, temp_node.state)
# #                 # print(temp_node.state.board)
# #                 # sleep(5)
# #                 if temp_node.state not in closed_list:
# #                     child_node = Node(deepcopy(temp_node.state), temp_node.g_value+1)
# #                     open_list.append(deepcopy(child_node))
# #                     # closed_list.append(temp_node.state)
# #         open_list.sort(key = lambda x:x.h_value,reverse=False)
# #         closed_list.append(parent_node.state)
# #         del open_list[0]


# from queue import Queue
# def ai_move(current_state: Board):
#     """
#         Bot (Artifical Intelligence plays the game)
#     Parameters:
#         current_state (Board obj): Current State of the board
#     Returns:
#         Returns if win state is achieved or not
#     """
#     queue = []
#     seen = []
#     # node = Node(current_state)
#     # queue.append(deepcopy(node))
#     # seen.append(current_state.board)
#     # tentative_hscore = float('inf')

#     queue = { str(current_state.board) : Node(current_state) }
#     closed_list = {}


#     while len(queue) != 0:
#         # queue.sort(key = lambda x:x.f_value,reverse=False)
#         node = get_best_node(queue)
#         closed_list[str(node.state.board)] = deepcopy(node)
#         del queue[str(node.state.board)]

#         # seen.append(node.state.board)
#         if node.h_value == 0:
#             return [1,2,3]

#         for i in range(4):
#             child_node = deepcopy(node.get_neighbor(i))

#             if child_node != None and (str(child_node.state.board) not in closed_list.keys() or str(node.state.board) in queue.keys() and queue[str(child_node.state.board)].f_value > node.f_value):
#                 queue[str(child_node.state.board)] = deepcopy(child_node)
#                 # seen.append(child_node.state.board)

# def get_best_node(queue):
#     firest_iter = True
#     for node in queue.values():
#         if firest_iter or node.f_value < best_f:
#             firest_iter = False
#             best_node = node
#             best_f = best_node.f_value
#     return best_node

class Node:
    def __init__(self,board : Board, parent = None):
        self.state = board
        self.parent = parent
        self.g_value = 0
        if parent != None:
            self.g_value = parent.g_value + 1
        self.h_value = self.hamming_distance(board, game.win_state)
        # self.f_value = self.g_value + self.h_value

    def f(self):
        return self.g_value+self.h_value

    def hamming_distance(self, state : Board, final: list):
        cost = 0 
        board_len = len(state.board)
        for i in range(board_len):
            for j in range(board_len):
                pos = self.get_pos(final, state.board[i][j])
                cost += abs(i - pos[0]) + abs(j - pos[1])
        return cost

    def get_pos(self, state : list, element):
        for i in range(len(state)):
            if element in state[i]:
                return (i, state[i].index(element))

    def get_neighbors(self):
        list_nodes = []
        for i in range(4):
            temp_node = deepcopy(self)
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

            if game.is_valid_move(x,y, len(self.state.board)):
                game.move(move, temp_node.state)
                node = Node(temp_node.state, self)
                list_nodes.append(node)
        return list_nodes

def get_best_nodes(open_list):
    first_iter = True
    for node in open_list.values():
        if first_iter or node.f() < best_f:
            first_iter = False
            best_node = node
            best_f = best_node.f()
    return best_node

def a_star(start_state: Board):
    open_list = { str(start_state.board) : Node(start_state)}
    closed_list = {}

    while len(open_list) > 0:
        exam_node = get_best_nodes(open_list)
        closed_list[str(exam_node.state.board)] = exam_node

        if exam_node.state.board == game.win_state:
            return (1,2,3)
        
        neighbors = exam_node.get_neighbors()

        for node in neighbors:
            # print(str(node.state.board) in closed_list.keys())
            # print(str(node.state.board) in open_list.keys())
            # print(open_list[str(node.state.board)].f_value < node.f_value)
            if str(node.state.board) in closed_list.keys() or str(node.state.board) in open_list.keys() and open_list[str(node.state.board)].f() < node.f():
                continue
            open_list[str(node.state.board)] = node
        del open_list[str(exam_node.state.board)]
    return None


