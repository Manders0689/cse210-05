import constants

from game.casting.cast import Cast
from game.casting.cycle1 import Cycle1
from game.casting.cycle2 import Cycle2
from game.casting.score import Score
from game.scripting.script import Script
from game.scripting.control_cycle1_actors_action import ControlCycle1ActorsAction
from game.scripting.control_cycle2_actors_action import ControlCycle2ActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    # create the cast
    cast = Cast()
    cast.add_actor("cycle1", Cycle1())
    cast.add_actor("cycle2", Cycle2())

    score1 = Score()
    score2 = Score()
    score1.set_position(Point(constants.MAX_X - 850, 0))
    score2.set_position(Point(constants.MAX_X - 200, 0))
    score1.add_points(1)
    score2.add_points(1)
    score1.set_player_name("Player One")
    score2.set_player_name("Player Two")
    cast.add_actor("score1", score1)
    cast.add_actor("score2", score2)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlCycle1ActorsAction(keyboard_service))
    script.add_action("input", ControlCycle2ActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()