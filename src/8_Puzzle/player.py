from abc import ABC
class Player(ABC):
    def __init__(self, ishuman : bool):
        self.__ishuman = ishuman

    def is_human(self):
        """
        Returns true if player is humna otherwise false
        """
        return self.__ishuman