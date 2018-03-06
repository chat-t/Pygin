from game_engine.scene import Scene
from elements.normal_behaviors.player_controller import PlayerController
from elements.normal_behaviors.game_objects.rectangle import Rectangle
from elements.normal_behaviors.game_objects.circle import Circle
from elements.normal_behaviors.game_objects.square_test import SquareTest
from elements.normal_behaviors.game_objects.square_test_falling import SquareTestFalling


class MainScene(Scene):

    def __init__(self):
        """
        Create the list of normal_behaviors and call the superclass constructor passing the list
        """
        self.normal_behaviors_list = [PlayerController()]

        super(MainScene, self).__init__(self.normal_behaviors_list)

