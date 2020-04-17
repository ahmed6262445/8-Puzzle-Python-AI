import puzzle as game
from copy import deepcopy,copy
from direction import Direction,Coordinate
from board import print_board
from main import clear
from time import sleep

class Node:
    def __init__(self,board : list, parent = None):
        self.state = board
        self.parent = parent
        self.g_value = 0
        if parent != None:
            self.g_value = parent.g_value + 1
        self.h_value = self.euclidean_distance(board, game.win_state)

    def f(self):
        return self.g_value+self.h_value

    def euclidean_distance(self, state : list, final: list) -> int:
        cost = 0 
        board_len = len(state)
        for i in range(board_len):
            for j in range(board_len):
                pos = self.get_pos(final, state[i][j])
                cost += abs(i - pos[0]) + abs(j - pos[1])
        return cost

    def get_pos(self, state : list, element):
        for i in range(len(state)):
            if element in state[i]:
                return (i, state[i].index(element))

    def get_neighbors(self):
        list_nodes = []
        for i in range(4):
            temp_state = deepcopy(self.state)
            x,y = game.find_empty_space(temp_state)

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

            if game.is_valid_move(x,y, len(temp_state)):
                temp_state = game.move(move, list(temp_state))
                if temp_state != None:
                    list_nodes += [Node(temp_state, self)]
        return list_nodes

def get_best_nodes(open_list : dict):
    first_iter = True
    for node in open_list.values():
        if first_iter or node.f() < best_f:
            first_iter = False
            best_node = node
            best_f = best_node.f()
    return best_node

def a_star(start_state: list):
    open_list = { str(start_state) : Node(start_state)}
    closed_list = {}

    while len(open_list) > 0:
        exam_node = get_best_nodes(open_list)
        closed_list[str(exam_node.state)] = exam_node

        if exam_node.state == game.win_state:
            print_path(exam_node)
            return True

        
        neighbors = exam_node.get_neighbors()

        for node in neighbors:
            if str(node.state) in closed_list.keys() or str(node.state) in open_list.keys() and open_list[str(node.state)].f() < node.f():
                continue
            open_list[str(node.state)] = node
        del open_list[str(exam_node.state)]
    return None


def array_to_str(arr : list):
    arr_str = ""
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr_str += str(arr[i][j])
    return arr_str

def generate_sequence(node : Node):
    nodes_list = []
    while(node != None):
        nodes_list.append(list(node.state))
        node = node.parent
    return nodes_list
    


def print_path(node):
    sequence = generate_sequence(node)
    goal_state = array_to_str(game.win_state)
    path =""
    for i in range(len(sequence)-1,-1,-1):
        board = print_board(sequence[i])
        path += array_to_str(sequence[i])
        path += "\n"
        sleep(1)
        clear()
        print(board)
        print(f"Goal state: {goal_state}")
        print(f"Steps taken: {len(sequence)-1}")
        print("Path taken: ")
        print(path)




