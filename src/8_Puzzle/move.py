from enum import Enum
from player import Player
from spot import Spot

class MoveOptions(Enum):
    def __init__(self, up :str ='w', down :str = 's', left :str = 'a', right :str = 'd'):
        """
        Sets the up, down, left, right movement options
        """
        self.up =  up 
        self.down = down
        self.right = right
        self.left = left

class Move():
    def __init__(self, player : Player, source : Spot, destination: Spot):
        self.__player = player
        self.__source = source
        self.__destination = destination

        self.__source_value = self.__source.value
        self.__destination_value = self.__destination.value