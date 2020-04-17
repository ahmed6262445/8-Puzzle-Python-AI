from random import randint
class Board():
    def __init__(self, length: int, breadth: int):
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
        self.__board = [[-1 for j in range(breadth)] for i in range(length)]
        self.initialize_board()
    
    def initialize_board(self):
        """
            This simply initializes the 8-Puzzle Board
            it does not neccassrily initialzes in asscending or descending order 
            e.g.
            0 | 1 | 2 
            3 | 4 | 5
            6 | 7 | 8
        """
        generated_list = []
        
        for i in range(self.__length):
            j = 0
            while j < self.__breadth:
                rand_num = randint(0,9)
                if not rand_num in generated_list:
                    generated_list.append(rand_num)
                    self.__board[i][j] = rand_num
                    j += 1
    
    def get_board(self) -> str:
        """
        Returns a string of the board
        """
        return self.__board