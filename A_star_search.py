import puzzle as game
from copy import deepcopy
from direction import Direction,Coordinate
from board import Board

class Node:
    def __init__(self,board : list, parent = None):
        self.state = board
        self.parent = parent
        self.g_value = 0
        if parent != None:
            self.g_value = parent.g_value + 1
        self.h_value = self.hamming_distance(board, game.win_state)

    def f(self):
        return self.g_value+self.h_value

    def hamming_distance(self, state : list, final: list) -> int:
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

            if game.is_valid_move(x,y, len(self.state)):
                state_move = game.move(move, temp_node.state)

                if state_move != None:
                    temp_node.state = state_move
                    node = Node(temp_node.state, self)
                    list_nodes.append(node)
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
    open_list = { str(start_state.list) : Node(start_state)}
    closed_list = {}

    while len(open_list) > 0:
        exam_node = get_best_nodes(open_list)
        closed_list[str(exam_node.state)] = exam_node

        if exam_node.state == game.win_state:
            return (1,2,3)
        
        neighbors = exam_node.get_neighbors()

        for node in neighbors:
            if str(node.state) in closed_list.keys() or str(node.state) in open_list.keys() and open_list[str(node.state)].f() < node.f():
                continue
            open_list[str(node.state)] = node
        del open_list[str(exam_node.state)]
    return None


