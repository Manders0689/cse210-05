from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def get_points(self):
        """Sets points for the user
        Returns:
        ---
            Integer: A point value for each player.
        """
        return self._points

    def reduce_points(self):
        """Reduces points for the user"""
        self._points -= 1
        self.set_text(f"{self._player_name}: {self._points}")

    def set_player_name(self,name):
        """Sets the player's name
        Args:
        ---
            name (string): gets the user inputted name
        """
        self._player_name = name
        self.set_text(f"{self._player_name}: {self._points}")