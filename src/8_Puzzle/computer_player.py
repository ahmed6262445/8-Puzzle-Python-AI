from player import Player

class ComputerPlayer(Player):
    def __init__(self, ishuman):
        """
        Calls abstract class Player's contructor to
        set calue for ishuman attribute
        """
        super(ComputerPlayer, self).__init__(ishuman) 