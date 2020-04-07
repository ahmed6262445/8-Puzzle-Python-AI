from random import randint
from numpy import reshape
class Board():
    def __init__(self, length: int, breadth: int, board = [[],[],[]]):
        """
        Parameters:
            length (int) : It sets the length of the board
            breadth (int): It sets the breadth of the board
        Members:
            lenght (int): Length of the board
            breadth (int): Breadth of the board
            board (list):  Board itself (It is initialzed by -1 invalide spots)
        """
        self.__length = length
        self.__breadth = breadth
        self.board = [[-1 for j in range(breadth)] for i in range(length)]
        self.initialize_board(board)
    
    def initialize_board(self, board):
        """`
            This simply initializes the 8-Puzzle Board
            it does not neccassrily initialzes in asscending or descending order 
            e.g.
            0 | 1 | 2 
            3 | 4 | 5
            6 | 7 | 8
        """
        self.board = reshape(board, (self.__length,self.__breadth))

    def print_board(self) -> str:
        """
        Returns a string of a printed board
        """
        board = ""
        for i in range(self.__length):
            for j in range(self.__breadth):
                board += str(self.board[i][j])
                if j != 2:
                    board += " | "
            board += "\n"
        return board