from player import Player

class HumanPlayer(Player):
    def __init__(self, ishuman):
        """
        Calls abstract class Player's contructor to
        set calue for ishuman attribute
        """
        super(HumanPlayer, self).__init__(ishuman) 