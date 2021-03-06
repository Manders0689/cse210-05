import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
        _winner (txt): Who won the game, or no one in the case of a tie
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_cycle_tail_collision(cast)
            self._handle_tail(cast)
            self._handle_cycle_collision(cast)
            self._handle_game_over(cast)

    def _handle_tail(self, cast):
        """"Handles how the cycles interact with the tails
        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """

        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        cycle1.grow_tail()
        cycle2.grow_tail()

    def _handle_cycle_tail_collision(self, cast):
        """Sets the game over flag if a cycle collides with the other cycle's tail
        and sets who won the game
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")

        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")

        cycle1_tail = cycle1.get_segments()[1:]
        cycle2_tail = cycle2.get_segments()[1:]
        cycle1_head = cycle1.get_head()
        cycle2_head= cycle2.get_head()

        # if cycle 2 hits cycle 1's tail, then cycle 1 wins
        for segment in cycle1_tail:
            if cycle2_head.get_position().equals(segment.get_position()):
                score2.reduce_points()
                if score2.get_points() < 1:
                    self._is_game_over = True
                    self._winner = "Player One"

            # If cycle_one hits its own tail, then displays cycle 2 wins
            if cycle1_head.get_position().equals(segment.get_position()):
                score1.reduce_points()
                if score1.get_points() < 1:
                    self._winner = "Player Two"
                    self._is_game_over = True

        # if cycle 1 hits cycle 2's tail, then cycle 2 wins
        for segment in cycle2_tail:
            if cycle1_head.get_position().equals(segment.get_position()):
                score1.reduce_points()
                if score1.get_points() < 1:
                    self._is_game_over = True
                    self._winner = "Player Two"        

            # If cycle_two hits its own tail, then displays cycle 1 wins
            if cycle2_head.get_position().equals(segment.get_position()):
                score2.reduce_points()
                if score2.get_points() < 1:
                    self._is_game_over = True
                    self._winner = "Player One"

    def _handle_cycle_collision(self, cast):
        """Sets the game over flag if a cycles collides with the other cycle and
        sets the winner as no one.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")

        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        head1 = cycle1.get_head()
        head2 = cycle2.get_head()

        if head1.get_position().equals(head2.get_position()):
            score1.reduce_points()
            score2.reduce_points()
            if score1.get_points() < 1 and score2.get_points() >= 1:
                self._is_game_over = True
                self._winner = "Player Two"
            elif score2.get_points() < 1 and score1.get_points() >= 1:
                self._is_game_over = True
                self._winner = "Player One"
            else:
                self._is_game_over = True
                self._winner = "No one"

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            cycle1 = cast.get_first_actor("cycle1")
            cycle2 = cast.get_first_actor("cycle2")
            cycle1_tail = cycle1.get_segments()
            cycle2_tail = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)


            if self._winner == "No one":
                message = Actor()
                message.set_text("Game over! It's a tie. Aim for the other cycle's tail and not the other cycle.")
                message.set_position(position)
                cast.add_actor("messages", message)
            else:
                message = Actor()
                message.set_text(f"Game Over! {self._winner} won!")
                message.set_position(position)
                cast.add_actor("messages", message)

            for segment in cycle1_tail:
                segment.set_color(constants.WHITE)

            for segment in cycle2_tail:
                segment.set_color(constants.WHITE)
