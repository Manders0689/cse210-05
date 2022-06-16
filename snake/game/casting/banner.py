class Banner(Actor):
    """
    A record of points made by the winning cycle and a game over message. 
    
    The responsibility of Score is to keep track of the winning player.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
