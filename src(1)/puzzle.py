from board import Board
from direction import Direction,Coordinate 

win_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

def move(direction: str, state) -> bool:
    """
        Gets the input to move the free space in the current state of the board (up, down, left, right)
    Parameter:
        direction (Direction enum) (int) Direction where the to move 
        state (Board): The current state of the board
    Return:
        returns if the move was made or not True is yes False if no move made
    """
    board_length = len(state.board)
    x, y = find_empty_space(state)
    
    increment_x = 0 
    increment_y = 0

    if direction == Direction.Up:
        increment_x, increment_y = Coordinate.Up.value
    elif direction == Direction.Down:
        increment_x, increment_y = Coordinate.Down.value
    elif direction == Direction.Left:
        increment_x, increment_y = Coordinate.Left.value
    elif direction == Direction.Right:
        increment_x, increment_y = Coordinate.Right.value

    x_new = x + increment_x
    y_new = y + increment_y

    is_valid = is_valid_move(x_new, y_new, board_length)

    if is_valid:        
        temp = state.board[x][y]
        state.board[x][y] = state.board[x_new][y_new]
        state.board[x_new][y_new] = temp
        return True
    return False

def find_empty_space(state) -> tuple:
    """
        Finds the empty location (0) value in the board
    Parameters:
        state (Board Obj): The current state of the board
    Return:
        returns a tuple of x and y co-ordination of empty location (0)
    """
    board_length = len(state.board)
    for i in range(board_length):
        for j in range(board_length):
            if state.board[i][j] == 0:
                return (i,j)

def is_valid_move(x:int, y:int,board_length) -> bool:
    """
        Finds if the move is possible or not on the board
    Parameters:
        x (int): x-coordinate of empty location on the board
        y (int): x-coordinate of empty location on the board
        direction (Direction enum) (int): Direction where the to move
        board_length (int): Length of the board
    Return:
        returns true (bool) if the move is possible else false (bool)
    """
    if x < 0 or y < 0 or x == board_length or y == board_length:
        return False
    return True

def invserion_count(state) -> int:
    """
        Counts how many of the tiles are misplaced from the right position
    Parameters:
        state (list): The current state of the board
    Return:
        Returns the cound of how many tiles are misplace from the right position
    """
    inv_count = 0
    board_len = len(state)
    for i in range(board_len):
        for j in range(i+1,board_len):
            if state[i] and state[j] and state[i] >= state[j]:
                inv_count += 1
    return inv_count

def is_solvable(state) -> bool:
    """
        Checks if the configuration of the board is solvable or not
    Parameters:
        state (list): The current state of the board
    Return:
        Returns true if the configuration is solvable
    """
    inv_count = invserion_count(state)
    return inv_count%2 == 0

def win_game(state) -> bool:
    """
        Returns if the game has been won or not
    Parameters:
        state (Board obj): The current state of the board
    Return:
        return True if current state of the board conforms with the wining state
    """
    if state.board == win_state:
        return True
    return False