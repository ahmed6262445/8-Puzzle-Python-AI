class Spot():
    def __init__(self, x: int, y: int, value):
        """
        Parameters:
            x : x-coordinate of the spot 
            y : y-coordinate of the spot
            value : Value assigned to a specfic spot on the board
        """
        self.__x = x
        self.__y = y
        self.__value = value

    # x-cordinate getter setters
    def set_x(self, x: int):
        """
        Sets the x-cordinate of the spot
        Parameter 
            x (int) : x-cordinate of the spot
        """
        self.__x = x
    def get_x(self) -> int:
        """
        Returns x-cordinate of the Spot
        """
        return self.__x

    # y-cordinate getter setters
    def set_y(self, y: int):
        """
        Sets the y-cordinate of the spot
        Parameter 
            y (int) : y-cordinate of the spot
        """
        self.__y = y
    def get_y(self) -> int:
        """
        Returns y-cordinate of the Spot
        """
        return self.__y

    # value getter setters
    def set_value(self, value):
        """
        Sets the value for the specific spot
        Parameters
            value (any data type) : Assigns a value to a specific spot
        """
        self.__value = value
    def get_value(self):
        """
        Returns a value for a specfic spot
        """
        return self.__value

    x = property(get_x,set_x)
    y = property(get_y,set_y)
    value = property(get_value,set_value)
