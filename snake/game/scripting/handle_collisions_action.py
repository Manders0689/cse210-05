class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the one cycle collides
    with the other cycle or the other cycle's trail, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

