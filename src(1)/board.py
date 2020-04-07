from random import randint
from numpy import reshape
from time import sleep
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
        self.board = []
        self.initialize_board(board)
    
    def initialize_board(self, board):
        """`
            Convertes the 1d List to 3d List 
            e.g.
            [1, 2 , 3, 4, 5 ,6 , 7, 8, 0]
            to
            0 | 1 | 2 
            3 | 4 | 5
            6 | 7 | 8
        """
        index = 0 # To keep track of index in the main loop
        for i in range(self.__length):
            temp_list = []
            for j in range(self.__breadth):
                temp_list.append(board[index])
                index += 1
            self.board.append(temp_list)

    def reshape_array(self,row: int, column: int, arr = []) -> list:
        pass

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