from random import randint
# from numpy import reshape
from time import sleep
class Board():
    def __init__(self, length: int, breadth: int, board):
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
        self.board =  list()
        self.initialize_board(board)

    def initialize_board(self, board):
        """
            Convertes the 1d List to 3d List 
            e.g.
            [1, 2 , 3, 4, 5 ,6 , 7, 8, 0]
            to
            0 | 1 | 2 
            3 | 4 | 5
            6 | 7 | 8
        """
        self.board = self.reshape_array(self.__length, self.__breadth, board)

    def reshape_array(self,row: int, col: int, arr = []) -> list:
        index = 0
        return_list = []
        for i in range(row):
            temp_list = []
            for j in range(col):
                temp_list.append(arr[index])
                index += 1
            return_list.append(temp_list)
        return return_list

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